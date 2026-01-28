# AI-Powered Assistive Navigation System 🦯

This is an AI-based project I built to explore how computer vision can be used to support visually impaired users during navigation.  
The system detects nearby objects using a camera, estimates their distance, and gives voice alerts when obstacles are too close.

---

## Why I Built This
While learning computer vision, I wanted to work on a project that solves a **real-world problem** instead of a generic dataset-based task.  
Navigation safety for visually impaired people felt meaningful and challenging, so I decided to build an assistive AI system around it.

---

## What the System Does
- Detects objects in real time using a webcam
- Estimates how far the object is from the user
- Gives voice warnings when objects are nearby
- Runs in real time with lightweight performance

---

## Technologies Used
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch
- Streamlit
- pyttsx3 (Text-to-Speech)

---

## How It Works (High Level)
1. The camera captures live video
2. YOLOv8 detects objects in each frame
3. Distance is estimated using bounding box size
4. Voice alerts are triggered when objects are close

---

## How to Run the Project Locally

### Step 1: Clone the repository
```bash
git clone https://github.com/SahithiPothagalla/AI-Assistive-Navigation.git
cd AI-Assistive-Navigation
