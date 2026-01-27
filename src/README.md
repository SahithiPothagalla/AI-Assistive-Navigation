# AI-Powered Assistive Navigation System for Visually Impaired

## 🔍 Problem Statement
Visually impaired individuals face challenges in detecting obstacles and estimating their distance in real time, which can lead to unsafe navigation.

## 💡 Solution
This project presents an AI-powered assistive navigation system that uses computer vision and deep learning to detect objects, estimate their distance, and provide real-time voice alerts to assist visually impaired users.

## 🧠 Features
- Real-time object detection using YOLOv8
- Distance estimation based on bounding box geometry
- Voice alerts for nearby obstacles
- Lightweight and real-time performance
- Designed with assistive technology principles

## 🛠️ Tech Stack
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch
- Text-to-Speech (pyttsx3)

## 🏗️ System Architecture
Camera → Object Detection → Distance Estimation → Voice Feedback

## ▶️ How to Run
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
