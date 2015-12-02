import pdb

def validNumber(phone_number):
	if len(phone_number) != 12:
		return False
	for i in range(12):
		if i in [3,7]:
			if phone_number[i] != '-':
				return False
		elif not phone_number[i].isdigit():
				return False
		return True


def validNumber2(phone_number):
	for (i,c) in enumerate(phone_number):
		if i in [3,7]:
			print(c)
			if c != '-':
				return False
		elif not c.isdigit():
				return False
	return True

def validNumber3(phone_number):
	if len(phone_number) != 14:
		return False
	for (i,c) in enumerate(phone_number):
		if(i==0):
			if(c!='('):
				return False
		elif(i==4):
			if(c!=')'):
				return False
		elif(i==5):
			if(c!=' '):
				return False
		elif(i==9):
			if(c!='-'):
				return False
		elif(not c.isdigit()):
				return False								
	return True

d = {0:'(', 4:')', 5:' ', 9:'-', '*':"isdigit()"}
def validNumber4(phone_number):
	if len(phone_number) != 14:
		return False
	for (i,c) in enumerate(phone_number):
		if i in d.keys():
			#print(d.get(i))
			if(c!=d.get(i)):
				return False
		elif(not eval("c." + d.get('*'))):		
		#elif(not c.isdigit()):
				return False								
	return True

	



#list1 = [[0, '('], [4, ')'], [5, ' '], [9, '-']]

#d = {0:'(', 4:')', 5:' ', 9:'-'}
#for key, value in d.items():
#	print(key, value)


print("validNumber", validNumber("123-123-1234"))
#pdb.set_trace()
res = validNumber2("123-123-1234")
print("validNumber2	", validNumber2("123-123-1234"))

print("validNumber3	", validNumber3("(123) 123-1234"))
print("validNumber4	", validNumber4("(123) 123-1234"))
#pdb.set_trace()


print(enumerate("123-123-1234"))
for i in enumerate("123-123-1234"):
	print(i)

#list1 = ((1,1), (2,2))
list1 = ([1,1], [2,2])
for i in list1:
	print(i)









