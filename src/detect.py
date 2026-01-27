from ultralytics import YOLO
import cv2
import pyttsx3
import time

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Distance estimation constants
KNOWN_WIDTH = 0.5      # meters
FOCAL_LENGTH = 615     # approximate webcam focal length
WARNING_DISTANCE = 2  # meters

# Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 160)

last_spoken_time = 0
SPEAK_COOLDOWN = 3  # seconds

def estimate_distance(bbox_width):
    if bbox_width == 0:
        return 0
    return (KNOWN_WIDTH * FOCAL_LENGTH) / bbox_width

def speak_warning(message):
    engine.say(message)
    engine.runAndWait()

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot access webcam")
    exit()

print("✅ Assistive AI started. Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            bbox_width = x2 - x1
            distance = estimate_distance(bbox_width)

            class_id = int(box.cls[0])
            label = model.names[class_id]

            text = f"{label} {distance:.2f}m"

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            # Voice alert logic
            current_time = time.time()
            if distance > 0 and distance < WARNING_DISTANCE:
                if current_time - last_spoken_time > SPEAK_COOLDOWN:
                    speak_warning(f"Warning, {label} at {distance:.1f} meters")
                    last_spoken_time = current_time

    cv2.imshow("AI Assistive Navigation - Voice Alerts", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
