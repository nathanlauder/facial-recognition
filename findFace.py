import cv2
import matplotlib as plt

defaultFrontalFaceCascadePath = r'./opencv/haarcascades/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(defaultFrontalFaceCascadePath)

def readImage(path):
  return cv2.imread(path)

def getGrayImage(imagePath):
    image = readImage(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./images/gray_image.jpg', gray)
    return gray

def findFace() -> None:
  imgPath = './images/image_143.jpg'
  gray = getGrayImage(imgPath)
  faces = cascade.detectMultiScale(
    gray,
    scaleFactor = 1.2,
    minNeighbors = 8,
    flags = cv2.CASCADE_SCALE_IMAGE
  )
  print("Found {0} faces in the image".format(len(faces)))

  image = readImage(imgPath)
  for (x, y, w, h) in faces:
    cv2.rectangle(
      image,
      (x, y),
      (x + w, y + h),
      (0, 0, 255),
      thickness = 3
    )
  
  cv2.imwrite('./images/rect_img.jpg', image)

# faces = getGrayImage('./images/image_143.jpg')
findFace()
# print(faces)
