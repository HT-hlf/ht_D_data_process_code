from PIL import Image
from PIL import ImageEnhance
import os
import cv2
import numpy as np
import random

# def move(root_path,img_name,off): #平移，平移尺度为off
#     img = Image.open(os.path.join(root_path, img_name))
#     offset = img.offset(off,0)
#     return offset
#
# def flip(root_path,img_name):   #翻转图像
#     img = Image.open(os.path.join(root_path, img_name))
#     filp_img = img.transpose(Image.FLIP_LEFT_RIGHT)
#     # filp_img.save(os.path.join(root_path,img_name.split('.')[0] + '_flip.jpg'))
#     return filp_img
#
# def rotation(root_path, img_name):  #旋转角度
#     img = Image.open(os.path.join(root_path, img_name))
#     rotation_img = img.rotate(20) #旋转角度
#     # rotation_img.save(os.path.join(root_path,img_name.split('.')[0] + '_rotation.jpg'))
#     return rotation_img

def randomColor(root_path, img_name): #随机颜色
    """
    对图像进行颜色抖动
    :param image: PIL的图像image
    :return: 有颜色色差的图像image
    """
    image = Image.open(os.path.join(root_path, img_name))
    random_factor = np.random.randint(0, 31) / 10.  # 随机因子
    color_image = ImageEnhance.Color(image).enhance(random_factor)  # 调整图像的饱和度
    random_factor = np.random.randint(10, 21) / 10.  # 随机因子
    brightness_image = ImageEnhance.Brightness(color_image).enhance(random_factor)  # 调整图像的亮度
    random_factor = np.random.randint(10, 21) / 10.  # 随机因子
    contrast_image = ImageEnhance.Contrast(brightness_image).enhance(random_factor)  # 调整图像对比度
    random_factor = np.random.randint(0, 31) / 10.  # 随机因子
    return ImageEnhance.Sharpness(contrast_image).enhance(random_factor)  # 调整图像锐度

def contrastEnhancement(root_path, img_name):  # 对比度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_con = ImageEnhance.Contrast(image)
    contrast = 1.5
    image_contrasted = enh_con.enhance(contrast)
    return image_contrasted

def brightnessEnhancement(root_path,img_name):#亮度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_bri = ImageEnhance.Brightness(image)
    brightness = random.randint(2,50)/100
    image_brightened = enh_bri.enhance(brightness)
    return image_brightened,brightness

def colorEnhancement(root_path,img_name):#颜色增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_col = ImageEnhance.Color(image)
    color = 1.5
    image_colored = enh_col.enhance(color)
    return image_colored

def rename(root_path,img_name):  #批量重命名
    image = Image.open(os.path.join(root_path, img_name))
    return image


imageDir = "test_image/raw"  #要改变的图片的路径文件夹
saveDir = "test_image/process"   #要保存的图片的路径文件夹
# i = 1
for name in os.listdir(imageDir):

    saveImage,brightness = brightnessEnhancement(imageDir,name)    #()前函数改成功能对应的函数名，即可使用
    saveName = "bright_" +str(brightness)+ name  # 保存的文件名
    saveImage.save(os.path.join(saveDir,saveName))
    # i = i + 1