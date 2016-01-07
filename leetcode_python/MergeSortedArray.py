#leetcode, Merge Sorted Array
#fix bug, consider j = -1

#import pdb

def merge(nums1, m, nums2, n):
    #for i in range(min(m,n)):
    i, j, k = m-1, n-1, m+n-1
    while(i>=0) and (j>=0):
        #if(k==0):
        #    pdb.set_trace()

        if(nums1[i]<=nums2[j]):
            nums1[k] = nums2[j]
            k, j = k-1, j-1
        else:
            nums1[k] = nums1[i]
            k, i = k-1, i-1

    while(j>=0):
        nums1[k] = nums2[j]
        k, j = k-1, j-1

    print(nums1)

a1 = [4,5,6, 0 , 0, 0]
a2 = [1,2,3]
merge(a1, 3, a2, 3)
