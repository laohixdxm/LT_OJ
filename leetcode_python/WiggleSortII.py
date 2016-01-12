#leetcode WiggleSortII, initial version
#fix bug, for test case arr = [1,5,1,1,6,4] without debugging


import pdb

# [1, 5, 1, 1, 6, 4] => [1, 4, 1, 5, 1, 6]
# [1, 3, 2, 2, 3, 1] => [2, 3, 1, 3, 1, 2]

'''
def d(index, start1, end1, start2, end2):
    if(start1<=index<=end1):
        return index-start1+start2
    if(start2<=index<=end2):
        return index-start2+start1
'''

def merge(nums, start1, end1, start2, end2):
    if(nums[start2] > nums[end1]):
        #switch two sub array,
        length = end1 - start1
        for i in range(end1 - start1+1):
            tmp = nums[start2+i]
            nums[start2+i] = nums[start1+i]
            nums[start1+i] = tmp

'''
        tmp = nums[orig]
        nums[orig] = nums[dest]
        while(d(orig)!=dest):
            tmp2 = nums[d(orig)]
            nums[d(orig)] = tmp
            
            tmp = tmp2
            orig = d(orig)
        nums[dest] = tmp
'''


def mergeSort(nums, start, end):
    #print(start, end)
    if(start==end):
        return
    elif(start+1==end):
        if(nums[start] > nums[end]):
            tmp = nums[end]
            nums[end] = nums[start]
            nums[start] = tmp
        return

    mid = (start+end)//2

    #pdb.set_trace()
    mergeSort(nums, start, mid)
    mergeSort(nums, mid+1, end)
    merge(nums, start, mid, mid+1, end)


def wiggleSort(nums):
    tmp = 0
    #
    for i in range(0, len(nums), 2):
        if(nums[i] > nums[i+1]):
            tmp = nums[i+1]
            nums[i+1] = nums[i]
            nums[i] = tmp

#arr = [2,1]
#arr = [1,2,3, 4, 5, 6, 7,8]

arr = [1,5,1,1,6,4]
#arr = [1,3, 2, 2, 3,1]
#wiggleSort(arr)
mergeSort(arr, 0, len(arr)-1)
print(arr)
    
    







