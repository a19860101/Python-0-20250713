import uuid, time, os

# img_name = uuid.uuid4()
img_name = str(int(time.time()*1000))

print(img_name)

print(os.path.dirname(os.path.abspath(__file__)))