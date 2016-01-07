#leetcode Delete Node in linked list

import pdb

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node):
#    while(node.next!= None):
    node.val = node.next.val
#        node = node.next
    node.next = node.next.next
    #print(node.val)
    #node = None

def deleteNode2(node):
    while(node.next!=None):
        node.val = node.next.val
        prev = node
        node = node.next
    prev.next = None


node1, node2, node3, node4= ListNode(1), ListNode(2), ListNode(3), ListNode(4)
node1.next, node2.next, node3.next = node2, node3, node4

#deleteNode(node3)
deleteNode2(node3)
#pdb.set_trace()
print(node1.val, node1.next.val, node1.next.next.val)
print(node1.next.next.next)




