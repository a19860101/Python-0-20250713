import glob
from PIL import Image
import os

image = glob.glob('./images/w*.jpg')
img = Image.open(image[0])

w,h = img.size
print(w, h)

w_s = 600
h_s = int((w_s * h) / w)

img_s = img.resize((w_s, h_s))

img.thumbnail((600,600))


os.makedirs('output', exist_ok=True)
img_s.save('./output/001.jpg', quality=75)
img.save('./output/002.jpg', quality=75)





