#bSearch: return the first bigger element if any


#bSearch: return the first bigger element if any
#pre is previous un-dup element
def bSearch(nums, pre, left, right):#nums already sorted
    if(left>right):
        return None

    mid = (left+right)//2
    #mid = math.ceil((left+right)/2)

    print(left, right, mid, nums[mid])
    if(nums[mid]>pre) and (nums[mid-1]==pre):
        print("..",pre)
        return nums[mid]
    elif(nums[mid-1]!=pre):
        return bSearch(nums, pre, left, mid-1)
    elif(nums[mid]==pre): 
        return bSearch(nums, pre, mid+1, right)


res= bSearch([1,1,2,3,3], 1, 2, 4)
print(res)

list1 = [1,1,2,3,3,4,5,5,5,6,6,6,6,6,6,6,7,7]
res= bSearch(list1, 4, 6, len(list1)-1)
print(res)

list1 = [1,1,2,3,3,4,4,4,4,4,4,4,4,4,4,4,6,7,7]
res= bSearch(list1, 4, 6, len(list1)-1)
print(res)

list1 = [1,1,2,2,2,2]
res= bSearch(list1, 2, 3, len(list1)-1)
print(res)

