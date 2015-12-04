#remove duplicate from linked list, linked list version, initial version

import pdb

'''
Given a sorted linked list, delete all duplicates such that each element appear only once. 
 
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 

#Given [1,1,2,3,3,4,5,5,5,6,7,7], return [1,2,3,4,5,6,7]
'''

class ListNode():
  def __init__(self, x):
    self.val = x
    self.next = None


def linkedlist(listOfNode):	
  for i in range(len(listOfNode)):
    if(i+1<len(listOfNode)):
      listOfNode[i].next = listOfNode[i+1]
    else:
      listOfNode[i].next = None  
  return listOfNode


def output_list(head):
  node = head
  i=0
  while(node!=None):
    print(node.val, "->", end="")
    node = node.next
    i+=1
    if(i==10):
      break
  print()


class Solution(object):
  def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    '''
    if head==None or head.next==None:
      return head
    p=head
    while p.next:
      if p.val==p.next.val:
        p.next=p.next.next
      else:
        p=p.next
    return head
    '''

    
    node1 = head    
    print(node1.val)#append node1
    while(node1!=None):
      node2=node1.next
      #node1.next=None
      while(node2!=None):
        if(node2.val>node1.val):
          print(node2.val)#append node2
          #pdb.set_trace()
          node1.next=node2
          node1 = node2
          break
        else:  
          node2=node2.next
      if(node1!=node2):
        node1=node1.next
    return head    
    

    '''
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
    '''



#print(nodeC.val)

list1 = linkedlist([ListNode(1), ListNode(1), ListNode(2)])
#print(list1[0].val)
output_list(list1[0])

s1=Solution()
res_head = s1.deleteDuplicates(list1[0])
output_list(res_head)


list2 = linkedlist([ListNode(1), ListNode(1), ListNode(2), ListNode(3), ListNode(3)])
res_head = s1.deleteDuplicates(list2[0])
output_list(res_head)

#res = s1.deleteDuplicates([1,1,2,3,3,4,5,5,5,6,7,7])
#print("...", res)

list3 = linkedlist([ListNode(1), ListNode(1), ListNode(2), ListNode(3), ListNode(3), 
  ListNode(4), ListNode(5), ListNode(5), ListNode(5), ListNode(6), ListNode(7), ListNode(7)])
res_head = s1.deleteDuplicates(list3[0])
output_list(res_head)
