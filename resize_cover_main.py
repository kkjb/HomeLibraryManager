# -*- coding: utf-8 -*-

from PIL import Image
import sys
import time
import os


def image_resize(src, dst, width=300):
    '''
    src: (str) 图片路径
    dst: (str) 保存路径
    width: (int) 宽度 (默认是300)
    '''
    # 读取图片
    img_ori = Image.open(src)
    w_ori = img_ori.size[0]
    h_ori = img_ori.size[1]

    w_percent = (width / float(w_ori))
    h_new = int((float(h_ori) * float(w_percent)))

    # img_new = img_ori.resize((width, h_new), Image.ANTIALIAS)
    # img_new = img_new.convert('P', palette=Image.ADAPTIVE, colors=256)

    # img_new = img_ori.convert('P', palette=Image.ADAPTIVE, colors=256)
    # img_new = img_new.resize((width, h_new), Image.ANTIALIAS)


    # only resize, the image shrinks via tinify 
    img_new = img_ori.resize((width, h_new), Image.ANTIALIAS)

    dst = os.path.splitext(dst)[0] + ".png"
    img_new.save(dst, optimize=True)





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

    # 删除遍历段，只找当前目录
'''
    for path, dir_list, file_list in os.walk(folder_name):
        for file_name in file_list:
            if file_name.endswith(('.png', '.jpg')):
                image_list.append(os.path.join(path, file_name))
                print(os.path.join(path, file_name))
                pass
'''




def batch_image_processing(image_list):


    for i in range(len(image_list)):
        path_tuple      = os.path.split(image_list[i])
        dirname         = path_tuple[0]
        basename        = path_tuple[1]
        new_image_path  = dirname + "\\new_image\\" + basename
        # convert to png format
        # move to along with the img_new.save
        #new_image_path = os.path.splitext(new_image_path)[0]+ ".png"

        image_resize(image_list[i], new_image_path,300)

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


    
