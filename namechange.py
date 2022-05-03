from email.mime import base
import imp
import os
import pathlib
import datetime
import pprint
import time
import platform
import re
from PIL import Image, ExifTags
import piexif

def PtoJ(input_path,output_dir):
   basename  = os.path.basename(input_path)
   im = Image.open(input_path)  
   im2 = im.convert("RGB")
   output_path = output_dir + '\\' + basename [:-4] + '.jpg'
   im2.save(output_path, "JPEG", quality=95)#クオリティ変えた方がいい？
   print(basename,'is converted to JPEG')

def GetDT(basename):
   stamp_list = re.split('[_.]',basename)
   the_date = stamp_list[2]
   the_time = stamp_list[3]
   the_date = the_date.split('-')
   the_time = the_time.split('-')
   the_dt = datetime.datetime(int(the_date[0]), int(the_date[1]), int(the_date[2]), int(the_time[0]), int(the_time[1]), int(the_time[2]),int(stamp_list[4]))
   return the_dt
   


def AddExif(input_path):
   basename = os.path.basename(input_path)
   basename = basename[:-4]
   dt = GetDT(basename)
   exif_dict = {}
   zeroth_ifd={}
   exif_ifd ={
      piexif.ExifIFD.DateTimeOriginal: dt.strftime("%Y:%m:%d %H:%M:%S"),
      piexif.ExifIFD.DateTimeDigitized: dt.strftime("%Y:%m:%d %H:%M:%S")} 
   gps = {}
   first_ifd={}
   exif_dict = {"0th":zeroth_ifd, "Exif":exif_ifd, "GPS":gps, "1st":first_ifd}
   exif_dict["Exif"]=exif_ifd
   exif_dict["GPS"] = gps
   exif_bytes = piexif.dump(exif_dict)
   piexif.insert(exif_bytes,input_path)
   print('Add TimeStamp to',basename)



p = os.getcwd()
p2 = p +'\\VRChat_1920x1080_2022-03-04_22-11-26.015.jpg' 

AddExif(p2)
