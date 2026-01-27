import streamlit as st

st.set_page_config(page_title="AI Assistive Navigation", layout="centered")

st.title("🦯 AI-Powered Assistive Navigation System")

st.subheader("🔍 What does this project do?")
st.write(
    "This system assists visually impaired users by detecting objects in real time, "
    "estimating their distance, and providing voice alerts for nearby obstacles."
)

st.subheader("🧠 Tech Stack")
st.write("- Python")
st.write("- YOLOv8 (Ultralytics)")
st.write("- OpenCV")
st.write("- PyTorch")
st.write("- Text-to-Speech (pyttsx3)")

st.subheader("🎯 Key Features")
st.write("- Real-time object detection")
st.write("- Distance estimation using computer vision")
st.write("- Voice-based obstacle alerts")
st.write("- Assistive technology focused design")

st.info(
    "⚠️ Live webcam and voice alerts run locally due to browser security restrictions."
)

st.subheader("▶️ How to Run Locally")
st.code("python src/detect.py", language="bash")

st.success("✅ Project is fully functional, deployed-ready, and resume-ready.")
