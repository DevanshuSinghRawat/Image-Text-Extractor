import numpy as np
import cv2, pytesseract
from PIL import ImageGrab
import pyperclip as ppc

def imToString():
    pytesseract.pytesseract.tesseract_cmd = R"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # while():
    # img = ImageGrab.grab(bbox =(700, 300, 1400, 900))
    img = ImageGrab.grabclipboard()
    # img=cv2.imread("test_img.png")
    tesstr= pytesseract.image_to_string( np.array(img), lang='eng')
    # tesstr= pytesseract.image_to_string(img)
    ppc.copy(tesstr)
    # print(tesstr)
    # img=ImageGrab.grabclipboard()
    cv2.imshow("clipboard img",np.array(img))
    cv2.waitKey()
 
imToString()
