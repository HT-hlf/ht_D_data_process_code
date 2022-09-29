import os

lh=sh=g=q=0
filepath='/media/htbao/xunfei/数据集制作/已制作数据集/sum_7_10/train/labels'
pathDir = os.listdir(filepath)
for s in pathDir:
	newDir = os.path.join(filepath, s)
	if os.path.isfile(newDir):
		if os.path.splitext(newDir)[1] == ".txt":
			with open(newDir, "r") as f:
				data = f.readlines()
				# print(int(data[0][0]))
				for i in range(len(data)):
					x=int(data[i][0])
					if x==0:
						lh+=1
					elif x==1:
						sh+=1
					elif x==2:
						g+=1
					else:
						q+=1

				# print(data)

print(lh)
print(sh)
print(g)
print(q)








# with open("/media/htbao/xunfei/数据集制作/D-数据集处理程序/glasses7.txt", "r") as f:
#     data = f.readlines()
#     print(int(data[0][0]))
#
#     print(data)