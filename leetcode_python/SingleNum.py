#leetcode, Single Number problem
#fix bug: double assignment
#related, python/xor.py


from random import randrange

def SingleNum(nums):
    num = nums[0]
    for i in range(1, len(nums)):
        num ^= nums[i]
    return num

nums1 = [2,3,2,4,3]
print(SingleNum(nums1))

nums2 = [0]*11
print(nums2)
for i in range(0, len(nums2)-1, 2):
    tmp = randrange(100), 
    nums2[i] = tmp 
    nums2[i+1] = tmp

nums2[len(nums2)-1] = randrange(101, 200,1)
print(nums2)

print(nums2, "num", SingleNum(nums2))