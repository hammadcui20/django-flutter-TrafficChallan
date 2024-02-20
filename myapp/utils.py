# smoking_detection_app/utils.py
from fastai.vision.all import *
import cv2

def smoking_(x):
    return 'Yes' if parent_label(x) == 'smoking' else 'No'

def predict_webcam(model_path):
    # Redefine the smoking_ function before loading the learner
    def smoking_(x):
        return 'Yes' if parent_label(x) == 'smoking' else 'No'
    learn = load_learner(model_path)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img = PILImage.create(frame)
        prediction, idx, probabilities = learn.predict(img)
        label = str(prediction)
        confidence = probabilities[idx].item()

        height, width, _ = frame.shape
        start_point = (0, 0)
        end_point = (width, height)
        color = (0, 255, 0)  # Green color
        thickness = 2
        frame = cv2.rectangle(frame, start_point, end_point, color, thickness)

        cv2.putText(frame, f"Prediction: {label}, Confidence: {confidence:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
