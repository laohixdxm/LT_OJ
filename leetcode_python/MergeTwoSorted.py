#leetcode, Merge Two Sorted Lists,
#too tricky, give up temporarily

#hold cur(current node), next1, next2 pointer, done

import pdb

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    next1, next2, cur = None, None, None
    if(l1.val<=l2.val):
        cur_list = 1        
        cur, next1, next2=l1, l1.next, l2
    else:
        cur_list = 2
        cur, next1, next2=l2, l1, l2.next 

    #pdb.set_trace()

    while(next1!=None) and (next2!=None):
        if(cur_list==1):
            if(next1.val<=next2.val): 
                cur, next1=cur.next, next1.next
                cur_list = 1
            else:
                cur.next, next2 = next2, next2.next
                cur = cur.next
                cur_list = 2
        elif(cur_list==2):
            if(next2.val<next1.val):
                cur, next2=cur.next, next2.next
                cur_list = 2
            else:
                cur.next, next1 = next1, next1.next
                cur = cur.next
                cur_list = 1

    if(next1!=None):
        cur.next = next1
    else:
        cur.next = next2

node1, node2, node3 = ListNode(1), ListNode(3), ListNode(5)
node1.next, node2.next = node2, node3

node4, node5, node6 = ListNode(2), ListNode(4), ListNode(6)
node4.next, node5.next = node5, node6

mergeTwoLists(node1, node4)
#pdb.set_trace()
node = node1
while(node!=None):
    print(node.val)
    node=node.next


