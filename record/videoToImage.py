import cv2

video = cv2.VideoCapture('./videos/recording.mp4')

success, image = video.read()
count = 1
while success:
  cv2.imwrite("./images/image_%d.jpg" % count, image)    
  success, image = video.read()
  print('Saved image ', count)
  count += 1