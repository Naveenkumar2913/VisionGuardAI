import cv2
import pickle
import numpy as np
from insightface.app import FaceAnalysis

# Load registered embeddings
with open("face_embeddings.pkl", "rb") as f:
    known_faces = pickle.load(f)

# Initialize InsightFace
app = FaceAnalysis()
app.prepare(ctx_id=0)

cap = cv2.VideoCapture(0)

THRESHOLD = 0.65

while True:
    ret, frame = cap.read()

    if not ret:
        break

    faces = app.get(frame)

    for face in faces:

        embedding = face.embedding

        best_name = "Unknown"
        best_score = -1

        for name, known_embedding in known_faces.items():

            similarity = np.dot(embedding, known_embedding) / (
                np.linalg.norm(embedding) *
                np.linalg.norm(known_embedding)
            )

            if similarity > best_score:
                best_score = similarity
                best_name = name

        if best_score < THRESHOLD:
            best_name = "Unknown"

        x1, y1, x2, y2 = map(int, face.bbox)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

        cv2.putText(
            frame,
            f"{best_name} ({best_score:.2f})",
            (x1, y1-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

    cv2.imshow("VisionGuard AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()