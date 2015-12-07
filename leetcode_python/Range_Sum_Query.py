#Range Sum Query - Immutable, initial version

#
'''
#Range Sum Query - Immutable

#Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

#Example:

#Given nums = [-2, 0, 3, -5, 2, -1]

#sumRange(0, 2) -> 1
#sumRange(2, 5) -> -1
#sumRange(0, 5) -> -3

#Note:

#    You may assume that the array does not change.
#    There are many calls to sumRange function.
'''

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if(i==j):
            return nums[i]
        mid=(i+j)//2
        return self.sumRange(i,mid) + self.sumRange(mid+1,j)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

nums = [-2, 0, 3, -5, 2, -1]
numArray1 = NumArray(nums)

#sumRange(0, 2) -> 1
print(numArray1.sumRange(0, 2))
#sumRange(2, 5) -> -1
print (numArray1.sumRange(2, 5))
#sumRange(0, 5) -> -3
print (numArray1.sumRange(0, 5))
#sumRange(0, 0) -> -2
print (numArray1.sumRange(0, 0))
#sumRange(5, 5) -> -1
print (numArray1.sumRange(5, 5))










