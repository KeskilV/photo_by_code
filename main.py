
from pyzbar.pyzbar import decode
from PIL import Image


decoded = decode(Image.open('img/IMG_6036.JPG'))
print(decoded[0].data.decode("utf-8"))