from ultralytics import YOLO
import cv2

from ultralytics import YOLO
import cv2

from zone import draw_zone,inside_zone

# Load the pretrained YOLO model
model = YOLO("yolov8n.pt")

# Open the default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run AI detection
    results = model.track(
    frame,
    persist=True,
    tracker="bytetrack.yaml",
    classes=[0]
)

    # Draw detections
    annotated_frame = results[0].plot()

    boxes = results[0].boxes

    if boxes is not None:
      for box in boxes:

        x1,y1,x2,y2 = box.xyxy[0]

        x1=int(x1)
        y1=int(y1)
        x2=int(x2)
        y2=int(y2)

        foot=( (x1+x2)//2 , (y1+y2)//2 )

    if inside_zone(foot):
            cv2.putText(annotated_frame,"ALERT!",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3 )

    draw_zone(annotated_frame)

    # Show the output
    cv2.imshow("VisionGuard AI - Person Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()