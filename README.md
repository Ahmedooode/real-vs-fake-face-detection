# 🧠 Anti-Spoofing Attendance System Using Face Mesh Technique

**Authors:**  
Ahmed Ehab Nasr  
Anas Abdelhadi Elhaj  
Zahir Tagalsr Osman

**Supervisor:** Mr. Mugtaba Abdalla Mohamed  
**Faculty:** Engineering Sciences, Omdurman Islamic University  
**Department:** Electrical and Electronics Engineering  
**Year:** 2024

---

## 📄 Abstract

This project presents the design and implementation of an **attendance system** that detects **real vs fake faces** using **computer vision** and **deep neural networks**.  
Traditional attendance methods can be easily manipulated by photos, videos, or masks — leading to security breaches.  
By leveraging **YOLOv8**, **Face Mesh (MediaPipe)**, and **Convolutional Neural Networks (CNN)** accelerated by **CUDA GPU processing**, the system achieves **high accuracy** in real-time antispoofing detection.

It provides:

- Accurate real-time identification.
- A graphical user interface (GUI) for login and attendance.
- A practical solution for **educational institutions** and secure facilities.

---

## 🎯 Objectives

- Develop a neural network capable of distinguishing **real** and **fake** faces in real time.
- Improve accuracy under variable lighting and facial angles.
- Integrate the system into a **smart attendance platform** using YOLOv8 + CNN.
- Prevent spoofing via printed images, video replays, and 3D masks.

---

## ⚙️ Methodology

1. **Face Feature Extraction:**  
   Using MediaPipe’s **Face Mesh**, 468 3D facial landmarks (x, y, z) were extracted.
2. **Model Training:**
   - Model: YOLOv8-Large (Ultralytics)
   - Framework: PyTorch
   - Training: GPU-accelerated (NVIDIA GTX 1050 Ti, CUDA 12)
3. **Offline Training:**  
   Dataset split into train/test with labeled classes (`real`, `fake`).
4. **Evaluation:**  
   Used **precision**, **recall**, **F1-score**, **accuracy**, and **confusion matrix**.
5. **Integration:**  
   Combined with a **face recognition system** and **attendance database (SQLite3)** for real-world usage.

---

## 🧩 Tools & Libraries

- **Python 3.x**
- **PyTorch**
- **OpenCV**
- **MediaPipe**
- **Ultralytics YOLOv8**
- **face_recognition**
- **SQLite3**
- **CUDA 12 (GPU acceleration)**
- **PyCharm IDE**

---

## 🧪 Experimental Setup

| Component           | Description               |
| ------------------- | ------------------------- |
| Device              | Lenovo Legion Y520        |
| GPU                 | NVIDIA GTX 1050 Ti (8 GB) |
| OS                  | Windows                   |
| Driver              | 560.94                    |
| IDE                 | PyCharm Professional      |
| Virtual Environment | Python venv               |

---

## 📊 Results

- **Model:** YOLOv8-Large (fine-tuned)
- **Accuracy:** ~97.8%
- **Precision-Recall Curve:** Stable at high confidence thresholds.
- **Confusion Matrix:** Successfully separated true positives and negatives.
- **Real-time FPS:** 30–60 on GPU.

---

## 🖥️ User Interface

- Developed with Python and OpenCV.
- GUI handles registration, login, and attendance recording.
- Displays alerts for spoofing attempts (fake faces blocked).
- Stores attendance logs securely in SQLite database.

---

## 🧠 System Architecture
