#leetcode containsDuplicateII

def containsDuplicate2(nums, k):
    list1 = {}
    for i in range(len(nums)):
        if(nums[i] not in list1):
            list1[nums[i]] = i 
        elif(i - list1[nums[i]] <= k):            
            return True
    return False        


print(containsDuplicate2([1,2,3], 3))
print(containsDuplicate2([1,2,3,1,4,5], 3))
print(containsDuplicate2([1,2,3,1,4,5], 2))




