import cv2
from time import perf_counter

MAX_FRAMES = 150

defaultFrontalFaceCascadePath = r'./opencv/haarcascades/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(defaultFrontalFaceCascadePath)
camera = cv2.VideoCapture(0)

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# writer = cv2.VideoWriter('./videos/recording.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width,height))

def detectFace(frame):
  faces = cascade.detectMultiScale(
    frame,
    scaleFactor = 1.3,
    minNeighbors = 7,
  )
  for (x, y, w, h) in faces:
    cv2.rectangle(
      frame,
      (x, y),
      (x + w, y + h),
      (0, 0, 255),
      thickness = 3
    )
  return frame



frameCount = 0
startTime = perf_counter()
while True:
    imageReady, frame = camera.read()
    #  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = detectFace(frame)
    #  writer.write(frame)

    cv2.imshow('Press \'q\' to quit', frame)
    frameCount += 1
    if cv2.waitKey(1) == ord('q'):
        break
stopTime = perf_counter()
totalTime = stopTime - startTime
print('FPS: {}'.format(round((frameCount / totalTime), 4)))

camera.release()
# writer.release()
cv2.destroyAllWindows()