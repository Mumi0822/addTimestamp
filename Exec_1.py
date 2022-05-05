import os
import glob
import change_lib

#現在VRChatフォルダ内にある全ての画像を別フォルダにコピーするスクリプト
in_dir = os.getcwd() + '\\VRChat'
out_dir = os.getcwd() + '\\VRChat_JPEG'
im_list = glob.glob(in_dir + '/**/*.png', recursive=True) 
for im_path in im_list:
    change_lib.changefunc(im_path,out_dir)
