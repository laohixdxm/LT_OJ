#bug1: (left+right)/2 => (left+right)//2 or math.ceil((left+right)/2)

#bug2: ... = > ( , , left, mid-1)
#	   ... = > ( , , mid+1, right)

#bug3: bSearch(nums, target, left, mid-1) => return bSearch(nums, target, left, mid-1)
#	   bSearch(nums, target, mid+1, right) => return bSearch(nums, target, mid+1, right)


'''
	elif(left==right):
		if(target!=nums[left]):
			return -1
	elif(right==left+1):
		if(not target in [nums[left], nums[right]]):
			return -1		
'''

import math

def bSearch(nums, target, left, right):#nums already sorted
	if(left>right):
		return False

	#mid = (left+right)//2
	mid = math.ceil((left+right)/2)

	print(left, right, mid, nums[mid])
	if(target==nums[mid]):
		print("..",target)
		return target
	elif(target<nums[mid]):
		return bSearch(nums, target, left, mid-1)
	elif(target>nums[mid]):	
		return bSearch(nums, target, mid+1, right)


nums = [1,3,4,5,7,9]
res = bSearch(nums, 8, 0, len(nums)-1)
print(res)

for target in nums:	
	res = bSearch(nums, target, 0, len(nums)-1)
	print("...", res)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
for target in testlist:	
	res = bSearch(testlist, target, 0, len(testlist)-1)
	print("...", res)








			