#encoding=UTF-8
import os



path='G:\B-数据集\焊缝+X-Ray数据集\GC10-DET_Alex Kim\\archive'



count=0
for i in range(1,11):
    dectory=path+'/'+str(i)
    list = os.listdir(dectory)
    for l in list:
        file=dectory+'/'+l
        if os.path.exists(file):
            count+=1
        #     print('no xml:',filename)
        #     # os.remove(filename)
print(count)
