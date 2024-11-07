import serial
import time

def control_led(emotion):
    ser = serial.Serial('COM3', 9600, timeout=1)  # Update with your Arduino port
    time.sleep(2)  # Wait for the serial connection to initialize

    # Mapping emotions to LED signals
    emotion_to_signal = {
        "happy": b'1',
        "neutral": b'2',
        "sad": b'3',
        "angry": b'4',
        "fear": b'5',
        "disgust": b'6'
    }

    signal = emotion_to_signal.get(emotion, b'2')  # Default to neutral if not found
    ser.write(signal)  # Send the signal to Arduino

    ser.close()
