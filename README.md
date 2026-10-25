# 👁️ VigilEye: Real-Time AI Driver Drowsiness & Fatigue Detection System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)](https://opencv.org/)
[![Dlib](https://img.shields.io/badge/dlib-68%20Face%20Landmarks-orange.svg)](http://dlib.net/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/rishwebb)

**VigilEye** is a real-time computer vision driver safety monitoring system designed to prevent road accidents caused by fatigue, drowsiness, and distraction. By analyzing facial landmark geometry at 60+ FPS, VigilEye computes the Eye Aspect Ratio (EAR) and mouth yawn frequency, triggering instant audio-visual alerts before accidents happen.

---

## ⚡ Key Highlights & Architecture

* **68-Point Facial Landmark Mapping**: Powered by dlib's pretrained facial shape predictor model for robust facial structure localization.
* **Eye Aspect Ratio (EAR) Computation**: Dynamically measures the vertical-to-horizontal eye distances. When EAR falls below a calibrated threshold for consecutive frames, a drowsiness state is registered.
* **Yawn Frequency & Micro-Sleep Tracking**: Accurately differentiates between normal blinking and micro-sleep events.
* **Low-Latency Audio Alerts**: Emits high-priority audible alarms to awaken the operator immediately upon fatigue detection.

```
       [Webcam / Dashcam Feed]
                 │
                 ▼
     [Dlib 68-Point Landmark Extraction]
                 │
         ┌───────┴───────┐
         ▼               ▼
   [Left Eye EAR]  [Right Eye EAR]
         │               │
         └───────┬───────┘
                 ▼
       [EAR Average Calculation]
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
[EAR >= 0.25 (Awake)]   [EAR < 0.25 for > 20 Frames]
                           │
                           ▼
                 🚨 [TRIGGER ALARM & LOG EVENT]
```

---

## 🛠️ Tech Stack & Requirements

| Component | Technology |
|---|---|
| **Core Logic** | Python 3.8+ |
| **Computer Vision** | OpenCV (`cv2`) |
| **Landmark Predictor** | Dlib (`shape_predictor_68_face_landmarks.dat`) |
| **Audio Alerting** | Playsound / Pygame Audio Engine |
| **Array Vectorization** | NumPy, SciPy Spatial Distance |

---

## 🚀 Quickstart & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/rishwebb/VigilEye-Driver-Safety-System.git
cd VigilEye-Driver-Safety-System
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Safety Monitor
```bash
python main.py
```

*Press `q` at any time to gracefully terminate the video stream.*

---

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
