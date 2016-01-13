#leetcode SingleNumIII, cannt solve, 

def SingleNumIII(nums):
    xor = nums[0]
    for i in range(1,len(nums)):
        xor ^= nums[i]
    print(xor)
    lowest = xor & (-xor)

    pair = [0,0]

    for i in range(len(nums)):
        if(nums[i] & lowest):
            pair[0] ^= nums[i]
        else:
            pair[1] ^= nums[i]
    return pair

nums1 = [1, 2, 1, 3, 2, 5]
print(SingleNumIII(nums1))