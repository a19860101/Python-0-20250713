import glob
# import PIL
from PIL import Image
import os

# image = glob.glob('./images/*.[Jj][Pp][Gg]')
image = glob.glob('./images/w*.jpg')

img = Image.open(image[0])

os.makedirs('output', exist_ok=True)
img.save('./output/001.jpg', quality=75)

# quality 0-100
# subsampling 0,1,2







