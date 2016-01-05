#leetcode containsDuplicate

def containsDuplicate(nums):
    list1 = {}
    for i in range(len(nums)):
        if(nums[i] not in list1):
            list1[nums[i]] = i 
        else:
            return True
    return False        


print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3]))