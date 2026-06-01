# ResQWave 🚑

An intelligent emergency vehicle signal override system that uses computer vision to detect ambulances in real time and automatically clears traffic signals — reducing response time and potentially saving lives.

Built as a hackathon project at NeuraX 2.0, CMR.

---

## 🚨 The Problem

Urban intersections with fixed-timer signals cause delays for emergency vehicles. Ambulances lose precious minutes waiting at red lights — time that can be the difference between life and death.

## 💡 The Solution

ResQWave detects emergency vehicles using a CNN-based camera system and overrides traffic signals in real time, giving ambulances a clear and safe path through intersections.

---

## 🛠️ Tech Stack

- Python, OpenCV — real-time vehicle detection
- CNN (Convolutional Neural Network) — ambulance classification
- Arduino (HC-SR04, LEDs) — traffic signal prototype
- TensorFlow/Keras — model training

---

## 📁 Project Structure

\`\`\`
ResQWave/
├── src/
│   ├── train_cnn.py        # CNN model training
│   ├── detector.py         # OpenCV real-time detection
│   └── arduino_comm.py     # Serial communication with Arduino
├── arduino/
│   └── traffic_control.ino # Arduino sketch
├── model/
│   └── resqwave_model.h5   # Saved CNN model
├── data/
│   └── (training images)
├── results/
├── main.py
└── requirements.txt
\`\`\`

---

## ⚙️ How It Works

1. Camera feed is processed in real time using OpenCV
2. CNN model classifies whether an ambulance is detected
3. On detection, Arduino receives a signal via serial communication
4. Traffic lights switch to green for the emergency vehicle's path

---

## 🔌 Hardware Setup

- Arduino Uno
- HC-SR04 Ultrasonic Sensor — simulates vehicle detection
- Red, Yellow, Green LEDs — simulates traffic lights

---

## 🚀 Running the Project

1. Install dependencies
\`\`\`
pip install -r requirements.txt
\`\`\`

2. Train the model (optional — pretrained model included)
\`\`\`
python src/train_cnn.py
\`\`\`

3. Run real-time detection
\`\`\`
python main.py
\`\`\`

---

## 🌍 Impact

- 🚑 Reduces ambulance waiting time at signals
- 🚦 Minimizes unnecessary congestion
- 🌍 Contributes to smart city traffic systems

---

## 🔮 Future Scope

- Replace ultrasonic with industrial radar sensors for lane-wise detection
- Scale CNN + OpenCV module for larger intersections
- Integrate with city-wide IoT traffic controllers

---

## 👩‍💻 Built By

Niveditha Katta — [GitHub](https://github.com/Nivedithakatta08) | [LinkedIn](https://www.linkedin.com/in/niveditha-katta-bb0a5a334)