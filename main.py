
from pyzbar.pyzbar import decode
from PIL import Image


decoded = decode(Image.open('1200434418110830.NgZ9ZTaRjFlRHpZnRh2z_height640.png'))#'img/817d189b-9f3e-4794-a76b-a73307bbaf4e.jpg'))
print(decoded[0].data.decode("utf-8"))