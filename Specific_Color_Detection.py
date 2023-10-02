import cv2
import numpy as np

selected_color = None
state = False

def mouse_callback(event, x, y, flags, param):
    global selected_color, state

    if event == cv2.EVENT_LBUTTONDOWN:
        selected_color = frame[y, x]
        print("Selected Color:", selected_color)
        state=True

cap = cv2.VideoCapture(0)

cv2.namedWindow("Video")
cv2.setMouseCallback("Video", mouse_callback)

while True:
    ret, frame = cap.read()

    lab_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if state:
        lab_color = cv2.cvtColor(np.uint8([[selected_color]]), cv2.COLOR_BGR2HSV)[0][0]
        
        lower_color = np.array([lab_color[0] - 10, lab_color[1] - 50, lab_color[2] - 50])
        upper_color = np.array([lab_color[0] + 10, lab_color[1] + 50, lab_color[2] + 50])

        mask = cv2.inRange(lab_frame, lower_color, upper_color)
        filtered_frame = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Video", filtered_frame)
    else:
        cv2.imshow("Video", frame)

    if cv2.waitKey(1) == ord('R') :
        selected_color = None
        state = False

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()