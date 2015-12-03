#remove duplicate linked list, list [] version
#fix bug: s1.deleteDuplicates([1,1,2,3,3]) => [1,2]


'''
Given a sorted linked list, delete all duplicates such that each element appear only once. 
 
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 
'''

class Solution(object):
  def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    removeDup = []
    i=0
    removeDup.append(head[i])
    while(i<len(head)):
      j=i+1
      while(j<len(head)):
        if(head[j] > head[i]):
          removeDup.append(head[j])
          i = j
          break
        j+=1
      if(i!=j):
        i+=1 
    return removeDup

s1 = Solution()
res = s1.deleteDuplicates([1,1,2])
print("...", res)

res = s1.deleteDuplicates([1,1,2,3,3])
print("...", res)

res = s1.deleteDuplicates([1,1,2,3,3,4,5,5,5,6,7,7])
print("...", res)




