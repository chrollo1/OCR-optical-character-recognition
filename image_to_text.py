from PIL import Image
import pytesseract
# import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe"

img = Image.open('test2.png')
img.show()
result = pytesseract.image_to_string(img)
print(result)

del img
