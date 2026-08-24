# 🛣️ RoadGuardAI

### AI-Powered Traffic Monitoring, Helmet Detection & License Plate Recognition System

RoadGuardAI is a Computer Vision-based traffic monitoring system built using **Python, YOLOv8, OpenCV, and EasyOCR**.

The system processes traffic video in real time, detects vehicles, identifies helmets, detects license plates, reads plate text using OCR, and allows traffic evidence to be saved directly from the application.

---

## 🚀 Features

- 🚗 Detects vehicles from traffic video using YOLOv8
- 🪖 Detects helmets using a custom trained YOLO model
- 🔢 Detects vehicle license plates using a custom YOLO model
- 🔍 Reads license plate text using EasyOCR
- 🎥 Processes traffic video frame by frame
- 🖥️ Displays real-time detection results
- 📸 Press **S** to save evidence screenshots
- ❌ Press **Q** to safely exit the application
- 💾 Automatically saves captured evidence with a timestamp

---

## 🧠 Technologies Used

- **Python**
- **YOLOv8**
- **Ultralytics**
- **OpenCV**
- **EasyOCR**


## ⚙️ How the System Works

1. A traffic video is loaded using OpenCV.
2. YOLOv8 detects vehicles in each frame.
3. The custom helmet detection model analyzes the frame.
4. The custom license plate detection model locates number plates.
5. Detected license plates are cropped from the frame.
6. EasyOCR reads the text from the cropped license plate.
7. Detection results and license plate information are displayed on the screen.
8. Pressing **S** saves the current frame as evidence.
9. Pressing **Q** closes the application.

---

## 📂 Project Structure

```text
RoadGuardAI/
│
├── main.py
├── helmet_best.pt
├── number_plate_best.pt
│
├── videos/
│   └── traffic.mp4
│
├── Violations/
│   └── Saved evidence screenshots
│
└── README.md

## 🛠️ Installation and Setup

### 1. Clone the Repository

Open Terminal or Command Prompt and run:

```bash
git clone https://github.com/AmanAgrawalAI/RoadGuardAI.git

## Navigate to the Project Folder
cd RoadGuardAI

## Install Required Libraries
pip install ultralytics opencv-python easyocr

## Make Sure Required Files Are Available Before running the project, make sure these files are available in the correct locations:

   main.py
   helmet_best.pt
   number_plate_best.pt
   videos/traffic.mp4

## Run the Project
python main.py
## The application will open a window and start processing the traffic video in real time.

🎮 Controls
Key	Function
S	Save the current frame as evidence
Q	Quit the application

📸 Evidence Saving

When you press S, the current detection frame is saved automatically inside the Violations folder with a timestamp-based filename
Example: <img width="848" height="480" alt="violation_1780328217" src="https://github.com/user-attachments/assets/f1433442-00d2-4d00-95d6-4066d9ce76e2">


🔍 Detection Pipeline
Traffic Video
      ↓
YOLOv8 Vehicle Detection
      ↓
Helmet Detection
      ↓
License Plate Detection
      ↓
License Plate Cropping
      ↓
EasyOCR Text Recognition
      ↓
Real-Time Detection Display
      ↓
Evidence Screenshot Saving

---

## 📸 Project Screenshots

###  Vehicle Detection

<img width="1053" height="626" alt="Screenshot 2026-08-24 205836" src="https://github.com/user-attachments/assets/62194251-c0bd-49e7-90f0-6910c8db31d4">


### 🪖 Helmet Detection

<img width="1057" height="628" alt="Screenshot 2026-08-24 215111" src="https://github.com/user-attachments/assets/eb16be74-9477-4f24-adf1-6c152ae98478">



### 🚘 License Plate Detection

<img width="1042" height="625" alt="Screenshot 2026-08-24 205747" src="https://github.com/user-attachments/assets/e3fe51f4-1889-4de0-a69f-a053859e594a">


### 🚨 Traffic Violation Monitoring

<img width="848" height="480" alt="violation_1780328217" src="https://github.com/user-attachments/assets/7b1ad1ca-5167-4160-82ca-d001e475194d">


---

## 🔮 Future Improvements

- Improve helmet detection accuracy
- Add automatic violation detection
- Improve license plate OCR accuracy
- Add vehicle tracking across multiple frames
- Store violation details in a database
- Add a web-based dashboard for monitoring traffic violations
- Send automatic alerts for detected violations

---

## 👨‍💻 Author

**Aman Agrawal**

Aspiring Data Scientist | AI & Computer Vision Enthusiast

---

## 📄 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, please consider giving it a star!
