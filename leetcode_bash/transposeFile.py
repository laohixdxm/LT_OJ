d = {}
fo = open("file3.txt", "r")

#d = {'name':'age', 'alice':21,'ryan':30}
for line in fo.readlines():
	tuple1 = tuple(line.split())

	d[tuple1[0]] = tuple1[1]

print("%-10s" %'name', end="")
for key,value in d.items():
	if(key != 'name'):	
		print("%-10s" %key, end="")
print()

print("%-10s" %d['name'], end="")
for key,value in d.items():
	if(key != 'name'):	
		print("%-10s" %value, end="")
print()

