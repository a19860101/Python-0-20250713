import glob
from PIL import Image
import os

images = glob.glob('./images/*.[Jj][Pp][Gg]') + glob.glob('./images/*.[Jj][Pp][Ee][Gg]') + glob.glob('./images/*.[Pp][Nn][Gg]') + glob.glob('./images/*.[Gg][Ii][Ff]')
# i=0
for i, image in enumerate(images):

    img = Image.open(image)

    w,h = img.size
    print(w, h)

    w_s = 600
    h_s = int((w_s * h) / w)

    os.makedirs('output', exist_ok=True)

    img_s = img.resize((w_s, h_s))

    # img.thumbnail((600,600))

    imgname = os.path.basename(image)
    _,ext = os.path.splitext(image)

    print(imgname[:-4])

    # img.save('./output/002.jpg', quality=75)
    # img_s.save(f'./output/0{i+1}.jpg', quality=75)
    img_s.save(f'./output/{imgname[:-4]}{ext}', quality=75)

    # i+=1




