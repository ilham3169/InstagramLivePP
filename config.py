# Import necessary modules
import PIL.Image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from time import strftime

img = PIL.Image.open("bg.jpeg")
img = img.resize((110, 110))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arialbd.ttf", 16)
draw.text((15, 40), f"{strftime('%Y-%m-%d')}", (0, 0, 0), font=font)
draw.text((33.5, 62), f"{strftime('%H:%M')}", (0, 0, 0), font=font)
img.save('sample-out.jpeg')
img.show()
