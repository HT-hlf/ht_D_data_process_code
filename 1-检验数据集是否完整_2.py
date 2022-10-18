#encoding=UTF-8
import os

# img_path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\VOCdevkit\VOC2007\JPEGImages'
# label_path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\VOCdevkit\VOC2007\Annotations'
# img_path=r"F:\Graduation_Design_Dataset\collect_RGBD\RGB-D_People_Dataset\rgbd_people_voc\sum\depth"
# label_path=r"F:\Graduation_Design_Dataset\collect_RGBD\RGB-D_People_Dataset\rgbd_people_voc\sum\annotation"

# img_path=r"G:\Internet_Dataset\recordData\RGBD_intelnet_b\rgb"
# label_path=r"G:\Internet_Dataset\recordData\RGBD_intelnet_b\annotation"

img_path=r"F:\doing\Motor_detection_dataset\third_dataset\labeled\dataset_dark_noise_1\image"
label_path=r"F:\doing\Motor_detection_dataset\third_dataset\labeled\dataset_dark_noise_1\label"

img_list=os.listdir(img_path)
label_list=os.listdir(label_path)

# for filename in img_list:
#     # print(filename.rstrip('png')+'xml')
#     filename_xml=label_path+'/'+filename.rstrip('jpg')+'xml'
#     # print(filename_xml)
#     if not os.path.exists(filename_xml):
#         print('no xml:',filename)
#         os.remove(img_path+'/'+filename)

for filename in img_list:
    filename_xml=label_path+'/'+filename.strip('jpg')+'txt'
    if not os.path.exists(filename_xml):
        print('no txt:',filename)
        os.remove(img_path+'/'+filename)

# for filename in img_list:
#     filename_xml=label_path+'/'+filename.strip('jpg')+'xml'
#     if not os.path.exists(filename_xml):
#         print('no xml:',filename)
#         os.remove(img_path+'/'+filename)


# for label in label_list:
#     filename_jpg=img_path+'/'+label.strip('xml')+'jpg'for label in label_list:
#     filename_jpg=img_path+'/'+label.rstrip('xml')+'jpg'
#     if not os.path.exists(filename_jpg):
#         print('no jpg:',label)
#         os.remove(label_path+'/'+label)
#     if not os.path.exists(filename_jpg):
#         print('no jpg:',label)
#         os.remove(label_path+'/'+label)

for label in label_list:
    filename_jpg=img_path+'/'+label.rstrip('txt')+'jpg'
    if not os.path.exists(filename_jpg):
        print('no jpg:',label)
        os.remove(label_path+'/'+label)

# for label in label_list:
#     filename_jpg=img_path+'/'+label.rstrip('xml')+'jpg'
#     if not os.path.exists(filename_jpg):
#         print('no jpg:',label)
#         # os.remove(label_path+'/'+label)