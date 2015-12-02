d={}
d2={}
'''
if(d.has_key(token)):
	d[token] += 1
else:
	d[token] = 1	
'''


fo = open("words.txt", "r")
for line in fo.readlines():
	tuple1 = tuple(line.split())
	for token in tuple1:
		if(token in d.keys()):
			d[token] += 1
		else:
			d[token] = 1	

print(d)

for (key,value) in d.items():
	d2[value] = key
print(d2)

for key in sorted(d.values(), reverse=True):
	print(d2[key], key)

#sorted(d2)

#print(sorted(d.values()))
#print(sorted(d, key=d.get))


#print(sorted(d.items()))
#print(sorted(d.items(), key=lambda x:x[1]))


	#print(line, end="")
#print()	



