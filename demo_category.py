import glob
###
list_anno_files = glob.glob('G:\B-数据集\C-数据集格式\yolov5\train\labels/*')

print(list_anno_files)

cate_list = []

for file_path in list_anno_files:
    with open(file_path) as file:
        anno_infos = file.readlines()

        print(anno_infos)

        for anno_item in anno_infos:
            cate_list.append(anno_item.split(' ')[0])

print(set(cate_list))