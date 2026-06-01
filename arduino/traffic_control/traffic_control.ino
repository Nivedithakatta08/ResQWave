// ResQWave - Smart Traffic Signal Override
// Controls LED traffic signals and reads ultrasonic sensor

// Traffic Light Pins
const int RED_PIN    = 8;
const int YELLOW_PIN = 9;
const int GREEN_PIN  = 10;

// Ultrasonic Sensor Pins
const int TRIG_PIN = 6;
const int ECHO_PIN = 7;

// Thresholds
const int PROXIMITY_THRESHOLD_CM = 50; // Override if vehicle within 50cm

void setup() {
    Serial.begin(9600);
    pinMode(RED_PIN,    OUTPUT);
    pinMode(YELLOW_PIN, OUTPUT);
    pinMode(GREEN_PIN,  OUTPUT);
    pinMode(TRIG_PIN,   OUTPUT);
    pinMode(ECHO_PIN,   INPUT);
    normalTraffic(); // Default state
}

void loop() {
    long distance = getDistance();
    Serial.print("Distance: ");
    Serial.println(distance);

    // Check serial signal from Python (CNN detection)
    if (Serial.available() > 0) {
        char signal = Serial.read();
        if (signal == '1') {
            emergencyOverride();
            delay(5000); // Hold green for 5 seconds
            normalTraffic();
        }
    }

    // Proximity-based override (ultrasonic backup)
    if (distance > 0 && distance < PROXIMITY_THRESHOLD_CM) {
        emergencyOverride();
        delay(3000);
        normalTraffic();
    }

    delay(100);
}

void emergencyOverride() {
    // All red except emergency path gets green
    digitalWrite(RED_PIN,    LOW);
    digitalWrite(YELLOW_PIN, LOW);
    digitalWrite(GREEN_PIN,  HIGH);
    Serial.println("EMERGENCY OVERRIDE ACTIVE");
}

void normalTraffic() {
    digitalWrite(GREEN_PIN,  LOW);
    digitalWrite(YELLOW_PIN, LOW);
    digitalWrite(RED_PIN,    HIGH);
}

long getDistance() {
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    long duration = pulseIn(ECHO_PIN, HIGH);
    return duration * 0.034 / 2; // Convert to cm
}