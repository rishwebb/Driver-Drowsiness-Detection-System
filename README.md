# AI Drowsiness Guard

This project is a real-time AI and Machine Learning based driver drowsiness detection system designed to monitor eye movements and yawning behavior through a webcam and provide instant audio alerts.

---

## Technology Used

* Python programming language
* OpenCV for computer vision processing
* Dlib machine learning model for facial landmark detection
* Eye Aspect Ratio algorithm for blink detection
* NumPy and SciPy for numerical calculations

---

## Main Features

* Real-time face detection using webcam
* Continuous eye blink monitoring
* Drowsiness alert system with audio alarms
* Yawn detection for fatigue monitoring
* Live webcam feed processing
* Cross-platform support for Windows and Linux

---

## Hardware Requirements

* Laptop or PC with a functional webcam
* Minimum 4GB RAM
* Processor capable of real-time video processing

---

## Software Requirements

* Python 3.x
* OpenCV
* Dlib
* NumPy
* SciPy
* Imutils
* Pygame

---

## Installation Guide

1. Clone or download the project folder.
2. Open a terminal inside the project directory.
3. Install the required dependencies using the following command:

pip install -r requirements.txt

---

## How to Run

After installation, execute the program with:

python main_final.py

Press the Q key to exit the application.

---

## Project Algorithm

* The system captures live video frames from the webcam.
* Facial landmarks are detected using the Dlib model.
* Eye Aspect Ratio (EAR) is calculated to detect eye closure.
* If eyes remain closed for multiple consecutive frames, a drowsiness alert is triggered.
* Mouth distance is measured to detect yawning behavior.
* Alerts are generated using audio notifications.
* Continuous monitoring ensures driver attentiveness and safety.

---

## Notes for Windows Users

* Ensure Python is added to PATH during installation.
* Install dependencies using pip install -r requirements.txt
* If webcam does not open, try changing camera index in the code.

---

## Disclaimer

This project is intended for educational and demonstration purposes only. It should not be solely relied upon for real-world driver safety without further testing and improvements.

---

## Author

Developed as a practical AI-based monitoring project using Python and Computer Vision techniques.

---

This README provides complete guidance to install, run, and understand the AI Drowsiness Guard project.
