import face_recognition as fr
import cv2 as cv
import numpy as np
import os

trainingDataPath = "../images/train"

knownNames = []
knownNameEncodings = []
trainingImages = os.listdir(trainingDataPath)

for img in trainingImages:
  imagePath = trainingDataPath + img
  image = fr.load_image_file(imagePath)
  encodedImage = fr.face_encodings(image)[0]
  knownNameEncodings.append(encodedImage)
  knownNames.append(os.path.splitext(os.path.basename(imagePath))[0].capitalize())

print(knownNames)
