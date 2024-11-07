import cv2
from fer import FER

def detect_emotion():
    detector = FER(mtcnn=True)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Detect emotions
        result = detector.detect_emotions(frame)
        if result:
            emotion, score = max(result[0]['emotions'].items(), key=lambda item: item[1])
            print(f"Detected emotion: {emotion} with score: {score}")

        # Display the frame
        cv2.imshow('Emotion Detector', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

detect_emotion()
