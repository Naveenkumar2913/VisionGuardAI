import cv2
import os

name = input("Enter person's name: ")

folder = "../known_faces"
os.makedirs(folder, exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not opened")
    exit()

print("Press SPACE to capture image")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Register Face", frame)

    key = cv2.waitKey(1)

    if key == 32:  # Space key
        filename = os.path.join(folder, f"{name}.jpg")
        cv2.imwrite(filename, frame)
        print("Face saved:", filename)
        break

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()