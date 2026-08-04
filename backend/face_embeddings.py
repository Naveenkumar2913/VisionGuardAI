import os
import pickle
import cv2
from insightface.app import FaceAnalysis

app = FaceAnalysis()
app.prepare(ctx_id=0)

KNOWN_FACES = "../known_faces"

embeddings = {}

for file in os.listdir(KNOWN_FACES):

    if file.lower().endswith((".jpg", ".jpeg", ".png")):

        name = os.path.splitext(file)[0]

        path = os.path.join(KNOWN_FACES, file)

        image = cv2.imread(path)

        faces = app.get(image)

        if len(faces) == 0:
            print(f"No face found in {file}")
            continue

        embeddings[name] = faces[0].embedding

        print(f"Registered: {name}")

with open("face_embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

print("Database saved successfully!")