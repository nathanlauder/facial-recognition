import cv2

cap = cv2.VideoCapture(0)

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width,height))

while True:
    ret,frame= cap.read()

    writer.write(frame)

    cv2.imshow('Video Capture', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()