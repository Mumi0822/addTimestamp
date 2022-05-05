import os
import datetime
import re
from PIL import Image
import piexif
import change_lib

#現在VRChatフォルダ内にある全ての画像を別フォルダにコピーするスクリプト
in_dir = os.getcwd() + '\\VRChat'
out_dir = os.getcwd() + '\\VRChat_JPEG'

AddExif(p2)
