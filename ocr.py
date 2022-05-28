import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\TesseractOCR\tesseract.exe"
img = cv2.imread("jk.jpg")
img = cv2.resize(img, None, fx=0.2,fy=0.2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray, 225,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
config = "--psm 4"
text = pytesseract.image_to_string(adaptive_threshold,config=config,
lang='eng')
print(text)
cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow('adaptive th',adaptive_threshold)
cv2.waitKey(0)