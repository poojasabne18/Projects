import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  #Path to extract

def convert():
    img= Image.open('img.png')
    text= pytesseract.image_to_string(img)
    print(text)

convert()