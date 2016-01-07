#leetcode, Merge Two Sorted Lists,
#too tricky, give up temporarily

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    node1, node2 = l1, l2
    if(node1.val<=node2.val):
        cur = 1
        #node1=node1.next
    else:
        cur = 2
        #node2=node2.next 

    while(node1!=None) and (node2!=None):
        if(cur==1):
            if(node1.next.val<=node2.val): 
                node1=node1.next
            else:
                node1_next = node1.next
                node1.next =node2
                node1 = node1_next
                cur = 2
        elif(cur==2):
            if(node2.next.val<node1.val):
                node2=node2.next
            else:
                node2_next = node2.next
                node2.next = node1
                node2 = node2_next
                cur = 1

node1, node2, node3 = ListNode(1), ListNode(3), ListNode(5)
node1.next, node2.next = node2, node3

node4, node5, node6 = ListNode(2), ListNode(4), ListNode(6)
node4.next, node5.next = node5, node6

mergeTwoLists(node1, node4)
node = node1
while(node!=None):
    print(node.val)
    node=node.next


