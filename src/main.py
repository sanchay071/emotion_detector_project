from emotion_detector import detect_emotion
from arduino_controller import control_led

def main():
    emotion = detect_emotion()
    control_led(emotion)

if __name__ == "__main__":
    main()
