
import cv2
import numpy as np

def region_of_interest(img):
    height = img.shape[0]
    polygons = np.array([
        [(0, height), (img.shape[1], height), (img.shape[1]//2, height//2)]
    ])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, polygons, 255)
    return cv2.bitwise_and(img, mask)

def detect_edges(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    return cv2.Canny(blur, 50, 150)

def detect_lane(frame):
    edges = detect_edges(frame)
    cropped_edges = region_of_interest(edges)

    lines = cv2.HoughLinesP(cropped_edges, 2, np.pi/180, 100,
                            np.array([]), minLineLength=50, maxLineGap=50)

    if lines is None:
        return frame, "No lane detected"

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)

    direction = "Straight"
    if lines[0][0][0] < lines[0][0][2]:
        direction = "Right"
    else:
        direction = "Left"

    cv2.putText(frame, f"Direction: {direction}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    return frame, direction
