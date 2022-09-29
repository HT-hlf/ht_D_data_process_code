#encoding=UTF-8
import os

# img_path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\VOCdevkit\VOC2007\JPEGImages'
# label_path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\VOCdevkit\VOC2007\Annotations'
# img_path='F:\毕设数据集\收集\VOC2028\JPEGImages'
label_path='Z:\ht_image'

# img_list=os.listdir(img_path)
label_list=os.listdir(label_path)


# for filename in img_list:
#     old_filename=img_path+'/'+filename
#     new_filename=img_path+'/a1_'+filename
#     os.rename(old_filename,new_filename)

# for filename in label_list:
#     old_filename=label_path+'/'+filename
#     new_filename=label_path+'/salt_noise_'+filename
#     os.rename(old_filename,new_filename)
for i ,filename in enumerate(label_list):
    old_filename=label_path+'/'+filename
    houzui=filename.split('.')[-1]
    new_filename=label_path+'/ht_'+ str(i)+'.'+houzui
    os.rename(old_filename,new_filename)
