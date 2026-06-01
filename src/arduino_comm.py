import serial
import time


class ArduinoComm:
    def __init__(self, port='COM3', baudrate=9600):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2)  # Wait for Arduino to initialize
            print(f"✅ Connected to Arduino on {port}")
        except serial.SerialException as e:
            print(f"⚠️  Could not connect to Arduino: {e}")
            self.ser = None

    def send_signal(self, signal: str):
        if self.ser and self.ser.is_open:
            self.ser.write(signal.encode())

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Arduino connection closed.")