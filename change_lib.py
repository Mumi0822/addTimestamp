import os
import datetime
import re
import shutil
from PIL import Image
import piexif

def PtoJ(input_path,output_dir):
   basename  = os.path.basename(input_path)
   im = Image.open(input_path)  
   im2 = im.convert("RGB")
   output_path = output_dir + '\\' + basename [:-4] + '.jpg'
   im2.save(output_path, "JPEG", quality=95)#クオリティ変えた方がいい？
   print(basename,'is copied')

def GetDT(basename):
   try:
      stamp_list = re.split('[_.]',basename)
      the_date = stamp_list[2]
      the_time = stamp_list[3]
      the_date = the_date.split('-')
      the_time = the_time.split('-')
      the_dt = datetime.datetime(int(the_date[0]), int(the_date[1]), int(the_date[2]), int(the_time[0]), int(the_time[1]), int(the_time[2]),int(stamp_list[4]))
   except:
      the_dt = None
   return the_dt
   
def AddExif(input_path):
   basename = os.path.basename(input_path)
   basename = basename[:-4]
   dt = GetDT(basename)
   if dt != None:
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
      ex_d =piexif.load(input_path)
      tcheck = ex_d["Exif"][piexif.ExifIFD.DateTimeOriginal]
      print('Add TimeStamp to',basename,'(',tcheck,')')
   else:
      Rdir = os.path.dirname(input_path)+'\\Rejected'
      os.makedirs(Rdir, exist_ok=True)
      shutil.move(input_path,Rdir)
      print(basename,'is Rejected!!')

def changefunc(in_path,out_dir):
   PtoJ(in_path,out_dir)
   im_path = out_dir+ '\\'+os.path.basename(in_path)[:-4] +'.jpg'
   AddExif(im_path)