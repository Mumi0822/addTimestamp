import os
import pathlib
import datetime
import time
import platform
from PIL import Image
from PIL.ExifTags import TAGS

p = pathlib.Path('F:\\files\\picture\\VRChat\\2022-04\\VRChat_1920x1080_2022-04-01_00-45-46.858.png')
#print(os.stat('sample.png'))
# os.stat_result(st_mode=33188, st_ino=8728494137, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=6, st_atime=1549094615, st_mtime=1549094615, st_ctime=1549094615)

#print(type(os.stat('sample.png')))
# <class 'os.stat_result'>
#dt = datetime.datetime.fromtimestamp(p.stat().st_ctime)
#print(dt)
def PtoJ():
   im = Image.open(p)
   exif = im._getexif(p)   
   im2 = im.convert("RGB")
   im2.save(exif.".jpg")


dic_ = {}
for id, value in exif.items():
   print(id, TAGS.get(id), value)