import cv2

ipv4_url = 'https://192.168.137.222:8080'
cam = f'{ipv4_url}/video'
cap = cv2.VideoCapture(cam)

while True:
    rect, frame = cap.read()
    frame = cv2.resize(frame, (600, 600))
    cv2.imshow("eye in the sky", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
