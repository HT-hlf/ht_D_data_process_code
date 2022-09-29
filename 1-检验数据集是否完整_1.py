#encoding=UTF-8
import os

# img_path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\VOCdevkit\VOC2007\JPEGImages'
# label_path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\VOCdevkit\VOC2007\Annotations'
# img_path=r"F:\Graduation_Design_Dataset\collect_RGBD\RGB-D_People_Dataset\rgbd_people_voc\sum\depth"
# label_path=r"F:\Graduation_Design_Dataset\collect_RGBD\RGB-D_People_Dataset\rgbd_people_voc\sum\annotation"

# img_path=r"G:\Internet_Dataset\recordData\RGBD_intelnet_b\rgb"
# label_path=r"G:\Internet_Dataset\recordData\RGBD_intelnet_b\annotation"

img_path=r"G:\mmdetection_miner\data\ht_cumt_rgbd_drise\depth_val"
label_path=r"G:\mmdetection_miner\data\ht_cumt_rgbd_drise\val2014"

img_list=os.listdir(img_path)
label_list=os.listdir(label_path)

for filename in img_list:
    # print(filename.rstrip('png')+'xml')
    filename_xml=label_path+'/'+filename
    # print(filename_xml)
    if not os.path.exists(filename_xml):
        print('no xml:',filename)
        os.remove(img_path+'/'+filename)
# for filename in img_list:
#     filename_xml=label_path+'/'+filename.strip('jpg')+'txt'
#     if not os.path.exists(filename_xml):
#         print('no txt:',filename)
#         os.remove(img_path+'/'+filename)

# for label in label_list:
#     filename_jpg=img_path+'/'+label.strip('xml')+'jpg'
#     if not os.path.exists(filename_jpg):
#         print('no jpg:',label)
#         os.remove(label_path+'/'+label)
for label in label_list:
    filename_jpg=img_path+'/'+label
    if not os.path.exists(filename_jpg):
        print('no jpg:',label)
        os.remove(label_path+'/'+label)