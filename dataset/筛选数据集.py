# coding:utf-8
__author__ = 'HT'

import os
import cv2
import shutil

path=r"F:\Graduation_Design_Dataset\collect\VOC2028\JPEGImages/"
path_useful=r'F:\Graduation_Design_Dataset\collect\ht_VOC2028\useful\image'
path_useless=r'F:\Graduation_Design_Dataset\collect\ht_VOC2028\useless\image'
def move_file(src_path, dst_path, file):
    try:
        # cmd = 'chmod -R +x ' + src_path
        # os.popen(cmd)
        f_src = os.path.join(src_path, file)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        f_dst = os.path.join(dst_path, file)
        shutil.move(f_src, f_dst)
    except Exception as e:
        print('move_file ERROR: ', e)

shut_down_count = False
for f in os.listdir(path):
    print(path + f)
    img = cv2.imread(path + f)
    print(path + f)
    while True:
        cv2.destroyAllWindows()
        cv2.waitKey(10)
        cv2.imshow('img_raw', img)
        waitkey_count = cv2.waitKey(1000000)
        # print(waitkey_count)
        # print(waitkey_count)
        if waitkey_count == 27:
            print('退出')
            shut_down_count = True
            break
        elif waitkey_count == 106:
            # print('j:有用')
            print('有用')
            move_file(path, path_useful, f)
            break
        elif waitkey_count == 107:
            # print('k：没用')
            print('没用')
            move_file(path, path_useless, f)
            # print(head_box)
            break
        else:
            pass

    if shut_down_count:
        break
