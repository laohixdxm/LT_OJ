file = open("file.txt", "r")

for i in range(1,11):
	line = file.readline()
	#print(i)
	if(i == 10):
		print(line)
