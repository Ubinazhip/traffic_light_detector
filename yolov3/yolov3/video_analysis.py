import numpy as np
import cv2

cap = cv2.VideoCapture('video_5.mp4')
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    i += 1
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if i == 276:
        cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()