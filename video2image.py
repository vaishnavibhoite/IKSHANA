import cv2
path = 'D:/projects/EDI_Ikshaana/video/project.mp4'
cap = cv2.VideoCapture(path)
ret = True
i = 0
j = 3772
while ret:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow('s', frame)
    if i % 5 == 0:
        cv2.imwrite('D:/projects/EDI_Ikshaana/video/center/'+str(j)+'.jpg', frame)
        j = j+1
    i = i+1
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cv2.destroyAllWindows()