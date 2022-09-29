#encoding=UTF-8
import shutil


# voc_path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\VOCdevkit\VOC2007\ImageSets\Main'
# train_txt='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\\2007_train.txt'
# test_txt='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\\2007_test.txt'
# JPEGImages='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\VOCdevkit\VOC2007\JPEGImages'
# labels='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit\VOCdevkit\VOC2007\labels'
# yolo_path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_yolov5'

voc_path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_VOCdevkit'
train_txt=voc_path+'/'+'2007_train.txt'
test_txt=voc_path+'/'+'2007_test.txt'
JPEGImages=voc_path+'/'+'VOCdevkit\VOC2007\JPEGImages'
labels=voc_path+'/'+'VOCdevkit\VOC2007\labels'
yolo_path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_yolov5'



voc_path_train=voc_path+'/VOCdevkit\VOC2007\ImageSets\Main'+'/'+'train.txt'
voc_path_test=voc_path+'/VOCdevkit\VOC2007\ImageSets\Main'+'/'+'test.txt'
# with open(voc_path_train,'r') as f:
#     lines =f.readlines()
#     for line in lines:
#         file_jpg=line.strip('\n')+'.jpg'
#         file_txt=line.strip('\n') + '.txt'
#         f_src=JPEGImages+'/'+file_jpg
#         # print(f_src)
#         f_dst=yolo_path+'/train/images/'+file_jpg
#         # print(f_dst)
#         # shutil.move(f_src, f_dst)
#         shutil.copyfile(f_src, f_dst)
#         f_src1 = labels + '/' + file_txt
#         # print(f_src)
#         f_dst1 = yolo_path + '/train/labels/' + file_txt
#         # print(f_dst)
#         # shutil.move(f_src1, f_dst1)
#         shutil.copyfile(f_src1, f_dst1)

with open(voc_path_test,'r') as f:
    lines =f.readlines()
    for line in lines:
        file_jpg=line.strip('\n')+'.jpg'
        file_txt=line.strip('\n') + '.txt'
        f_src=JPEGImages+'/'+file_jpg
        # print(f_src)
        f_dst=yolo_path+'/valid/images/'+file_jpg
        # print(f_dst)
        # shutil.move(f_src, f_dst)
        shutil.copyfile(f_src, f_dst)
        f_src1 = labels + '/' + file_txt
        # print(f_src)
        f_dst1 = yolo_path + '/valid/labels/' + file_txt
        # print(f_dst)
        # shutil.move(f_src1, f_dst1)
        shutil.copyfile(f_src1, f_dst1)