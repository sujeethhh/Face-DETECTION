import cv2
import os
from deepface import DeepFace

ENCODINGS_DIR = "face_encodings"
if not os.path.exists(ENCODINGS_DIR):
    os.makedirs(ENCODINGS_DIR)

def register_face(name):
    cap = cv2.VideoCapture(0)
    print(f"📷 Capturing face data for {name}... Look at the camera.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ ERROR: Cannot access webcam.")
            break

        cv2.imshow("Register Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to capture the face
            file_path = os.path.join(ENCODINGS_DIR, f"{name}.jpg")
            cv2.imwrite(file_path, frame)
            print(f"✅ Face registered successfully for {name}!")
            break

    cap.release()
    cv2.destroyAllWindows()

register_face("YourName")  # Change this when registering different users
