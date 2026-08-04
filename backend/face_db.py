import face_recognition
import os

known_encodings = []
known_names = []

folder = "../known_faces"

for file in os.listdir(folder):
    if file.endswith(".jpg") or file.endswith(".png"):
        image = face_recognition.load_image_file(os.path.join(folder, file))
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(os.path.splitext(file)[0])

print("Loaded:", known_names)