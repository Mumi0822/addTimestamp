import os
import pathlib
import datetime
import time
import platform
from PIL import Image
from PIL.ExifTags import TAGS
#p = pathlib.Path('F:\\files\\picture\\VRChat\\2022-04\\VRChat_1920x1080_2022-04-01_00-45-46.858.png')
#print(os.stat('sample.png'))
# os.stat_result(st_mode=33188, st_ino=8728494137, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=6, st_atime=1549094615, st_mtime=1549094615, st_ctime=1549094615)

#print(type(os.stat('sample.png')))
# <class 'os.stat_result'>
#dt = datetime.datetime.fromtimestamp(p.stat().st_ctime)
#print(dt)
# #for id, value in exif.items():
#   print(id, TAGS.get(id), value)
def PtoJ(input_path,output_dir):
   basename  = os.path.basename(input_path)
   im = Image.open(input_path)  
   im2 = im.convert("RGB")
   output_path = output_dir + '\\' + basename [:-4] + '.jpg'
   im2.save(output_path, "JPEG", quality=95)#クオリティ変えた方がいい？
   print(basename,'is converted to JPEG')

def AddExif(input_path,output_dir):
   basename = os.path.basename(input_path)
   basename = basename[:-4]
   stamp_list = basename.split('_')
   for stamp in stamp_list:
      print(stamp)
   print('Add TimeStamp to',basename)


p = os.getcwd()
p2 = p +'\\VRChat_1920x1080_2022-03-04_22-11-26.015.png' 
AddExif(p2,p)
