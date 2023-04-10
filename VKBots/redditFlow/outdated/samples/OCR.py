import pytesseract
from PIL import Image

tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('text.jpg'))
print(text)
input()
