import cv2
import numpy as np
from tensorflow.keras.models import load_model
from src.arduino_comm import ArduinoComm

CONFIDENCE_THRESHOLD = 0.85
MODEL_PATH = "model/resqwave_model.h5"

def preprocess_frame(frame):
    img = cv2.resize(frame, (64, 64))
    img = img / 255.0
    return np.expand_dims(img, axis=0)


def run_detector(use_arduino=False):
    model = load_model(MODEL_PATH)
    cap = cv2.VideoCapture(0)  # 0 = webcam

    arduino = None
    if use_arduino:
        arduino = ArduinoComm(port='COM3', baudrate=9600)

    print("ResQWave detector running. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        input_frame = preprocess_frame(frame)
        prediction = model.predict(input_frame, verbose=0)[0][0]
        is_ambulance = prediction >= CONFIDENCE_THRESHOLD

        label = f"AMBULANCE DETECTED ({prediction:.2f})" if is_ambulance else f"No Emergency ({prediction:.2f})"
        color = (0, 0, 255) if is_ambulance else (0, 255, 0)

        cv2.putText(frame, label, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        cv2.rectangle(frame, (10, 10), (frame.shape[1]-10, frame.shape[0]-10), color, 3)
        cv2.imshow("ResQWave - Emergency Vehicle Detector", frame)

        # Signal Arduino
        if use_arduino and arduino:
            arduino.send_signal("1" if is_ambulance else "0")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    if arduino:
        arduino.close()