import datetime
import os
import 
import glob
import change_lib

#最新の画像のみをJPEGとしてコピーするスクリプト
TODAY = datetime.date.today()
fname = TODAY.strftime('%Y-%m')
in_dir = os.getcwd() + '\\VRChat\\' + fname
out_dir = os.getcwd() + '\\VRChat_JPEG'
im_list = glob.glob(in_dir + '/**/*.png', recursive=True) 
for im_path in im_list:
    change_lib.changefunc(im_path,out_dir)
    


