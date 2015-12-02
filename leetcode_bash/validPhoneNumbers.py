def format1(phone):
	if(len(phone)!=12):
		return False

	for i in range(len(phone)):
		char_status = False		
		if((i==3) or (i==7)):
			if(phone[i] != '-'):
				return False	
		else:
			for j in range(10):				
				#print(phone[i], j)
				if(int(phone[i]) == j):
					char_status = True
					break					
			if(char_status == False):
				return False
	return True
					

def format2(phone):
	if(len(phone)!=14):
		return False

	for i in range(len(phone)):
		char_status = False		
		if(i==0):
			if(phone[i] != '('):
				return False
		elif(i==4):
			if(phone[i] != ')'):
				return False
		elif(i==5):
			if(phone[i] != ' '):
				return False					
		elif(i==9):
			if(phone[i] != '-'):
				return False		
		else:
			for j in range(10):				
				#print(phone[i], j)
				if(int(phone[i]) == j):
					char_status = True
					break					
			if(char_status == False):
				return False
	return True

#format1("123-123-1234")

file = open("file2.txt", "r")

#	num = file.readline().strip()
lines = file.readlines()
for line in lines:
	phone = line.strip()
	if(format1(phone) or format2(phone)):
	#if(format1(phone)):
		print(phone)


#for j in range(10):
#	print(j)

print(len("123-123-1234"))

phone="123-123-1234"
if(int(phone[1])==2):
	print("...")

