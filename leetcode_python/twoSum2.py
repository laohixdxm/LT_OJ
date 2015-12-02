#twoSum brute force version, with class usage

'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 
'''

numbers = [1,4,3,2,7,11,15]
target = 9


class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		i = 0
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				if(target==nums[i]+nums[j]):
					print("index=%d, index2=%d" %(i+1,j+1))
					return [i+1, j+1]
				else:	
					j+=1
			#print(i)
			i+=1


s1 = Solution()
res= s1.twoSum(numbers, target)
print(res)

res= s1.twoSum([3,2,4], 6)
print(res)




        