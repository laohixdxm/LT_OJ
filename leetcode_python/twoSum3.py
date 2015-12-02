#twoSum binary search version

#fix bug1: binary search should be on the sorted list



'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 
'''

import pdb

numbers = [1,4,3,2,7,11,15]
target = 9

class Solution(object):

	def bSearch(self, nums, target, left, right):#nums already sorted
		if(left>right):
			return None

		mid = (left+right)//2
		if(target==nums[mid]):
			return mid
		elif(target<nums[mid]):
			return self.bSearch(nums, target, left, mid-1)
		elif(target>nums[mid]):	
			return self.bSearch(nums, target, mid+1, right)


	def getIndex(self, nums, target):
		i = 0	
		while(i<len(nums)):
			if(nums[i]==target):
				return i
			i+=1


	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		numsSorted = sorted(nums)
		i = 0
		for i in range(len(numsSorted)):
			j = target - numsSorted[i]

			bSearchRet = self.bSearch(numsSorted, j, i+1, len(numsSorted)-1)
			if(bSearchRet!=None):	
				print(numsSorted)
				print("Sorted index=%d, index2=%d" %(i+1, bSearchRet+1))
				Index1 = self.getIndex(nums, numsSorted[i]) + 1
				
#				if(numsSorted[bSearchRet]==-3):	
#					pdb.set_trace()
				debug = self.getIndex(nums, numsSorted[bSearchRet])
				print("debug", debug, numsSorted[bSearchRet])

				Index2 = self.getIndex(nums, numsSorted[bSearchRet]) + 1
				
				print("...", Index1, Index2)
				if(Index1>Index2):
					return [Index2, Index1]
				else:
					return [Index1, Index2]	
			i+=1


s1 = Solution()
res= s1.twoSum(numbers, target)
print(res)

res= s1.twoSum([3,2,4], 6)
print(res)

res= s1.twoSum([0,4,3,0], 0)
print(res)












