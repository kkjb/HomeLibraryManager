# -*- coding: utf-8 -*-


import time
import os
import urllib.request
import requests
import datetime
import sys
import tinify

# You should change this to your API key

tinify.key = "NFKk611fT5YqddL4cpR1DxJ9tfZq3bSM" # 此处填入你自己申请的API key

# API upload 
def image_shrink(src, dst):
    '''
    src: (str) 图片路径
    dst: (str) 保存路径

    '''
    # 使用本地文件上传
    source = tinify.from_file(src)
    source.to_file(dst)

    # # 使用二进制上传
    # with open("unoptimized.jpg", 'rb') as source:
    #     source_data = source.read()
    #     result_data = tinify.from_buffer(source_data).to_buffer()

    # # 使用url上传
    # source = tinify.from_url("https://cdn.tinypng.com/images/panda-happy.png")
    # source.to_file("optimized.jpg")



# 遍历寻找图片
def walk_folder_for_images(folder_name):
    
    # detect and make directory
    new_image_folder_name = os.path.join(folder_name,"new_image")
    if os.path.exists(new_image_folder_name):
        print("new_image directory already exists.\n")
        pass
    else:
        os.makedirs(new_image_folder_name) 
    pass

    # find png and jpg images in this folder
    #  

    image_list = []

    # os.listdir(folder_name) 遍历当前目录文件

    file_list = os.listdir(folder_name)
    for file_name in file_list:
         if file_name.endswith(('.png', '.jpg', '.jpeg', 'bmp', 'tif', 'gif', 'tiff')):
            image_list.append(os.path.join(folder_name, file_name))
            print(os.path.join(folder_name, file_name))
        
    return image_list

def batch_image_processing(image_list):


    for i in range(len(image_list)):
        path_tuple      = os.path.split(image_list[i])
        dirname         = path_tuple[0]
        basename        = path_tuple[1]
        new_image_path  = dirname + "\\new_image\\" + basename
        # convert to png format
        # move to along with the img_new.save
        #new_image_path = os.path.splitext(new_image_path)[0]+ ".png"

        image_shrink(image_list[i], new_image_path)

    os.system("pause")

    pass


path_name = ''

if __name__ == "__main__":

    if len(sys.argv) != 2:

        path_name = input(' Please drag the image directory into the command line window:\n (only for jpg and png format files)\n')
        
        if path_name == '':
            print("no input")
            time.sleep(5)
            exit()
        else:
            image_list = walk_folder_for_images(path_name.strip('"'))
            batch_image_processing(image_list)

    else:

        path_name = sys.argv[1].strip('"')

        image_list = walk_folder_for_images(sys.argv[1].strip('"'))
        batch_image_processing(image_list)


    