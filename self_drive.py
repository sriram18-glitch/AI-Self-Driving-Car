
import cv2
from lane_detection import detect_lane

cap = cv2.VideoCapture(0)  # webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame, direction = detect_lane(frame)

    cv2.imshow("AI Self-Driving Car - Lane Detection", processed_frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
