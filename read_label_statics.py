import os



filepath=r'F:\doing\Motor_detection\datasets_second_remove_noise_add_third_check_add_aug\motor_detection_dataset_v2\labels\val2017'

class_name = ['y0','y1','y2','y3','w0','w1','w2','w3','scratch','shed','bolt']
class_count= [0 for i in class_name]
pathDir = os.listdir(filepath)
for s in pathDir:
	if s== 'classes.txt':
		continue
	# s='3633_36.txt'
	print(s)
	newDir = os.path.join(filepath, s)
	if os.path.isfile(newDir):
		if os.path.splitext(newDir)[1] == ".txt":
			with open(newDir, "r") as f:
				data = f.readlines()
				# print(data)
				# print(int(data[0][0]))
				for i in range(len(data)):
					data_i_split=data[i].split()
					x=int(data_i_split[0])
					print(x)
					class_count[x]+=1

				# print(data)

print(class_name)
print(class_count)








