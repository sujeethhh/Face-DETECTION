import cv2
import os
from deepface import DeepFace

ENCODINGS_DIR = "face_encodings"

def recognize_face():
    print("📷 Opening webcam... Look at the camera.")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ ERROR: Cannot access webcam.")
            break

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to capture
            file_path = "temp.jpg"
            cv2.imwrite(file_path, frame)
            print("🔍 Captured image. Matching against stored faces...")

            for filename in os.listdir(ENCODINGS_DIR):
                if filename.endswith(".jpg"):
                    registered_face = os.path.join(ENCODINGS_DIR, filename)

                    try:
                        result = DeepFace.verify(img1_path=file_path, img2_path=registered_face)
                        if result["verified"]:
                            name = filename.split(".")[0]
                            print(f"✅ Access Granted: {name}")
                            cap.release()
                            cv2.destroyAllWindows()
                            return name
                    except:
                        continue

            print("❌ Access Denied")
            break

    cap.release()
    cv2.destroyAllWindows()

recognized_user = recognize_face()
if recognized_user:
    print(f"Welcome, {recognized_user}!")
else:
    print("Failed to authenticate.")
