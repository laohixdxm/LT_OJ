#leetcode, Intersection of Two Linked Lists 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    list1, list2 = [], []
    node = headA
    while(node!=None):
        list1.append(node)
        node = node.next
    node = headB
    while(node!=None):
        list2.append(node)
        node = node.next
    cur = None
    while 1:
        node1 = list1.pop()
        node2 = list2.pop()
        #print(node1.val, node2.val)
        if(node1 is node2):
            cur = node1
        else:
            break
    return cur

node1, node2 = ListNode('a1'), ListNode('a2')
node3, node4, node5 =  ListNode('b1'), ListNode('b2'), ListNode('b3')
node6, node7, node8 = ListNode('c1'), ListNode('c2'), ListNode('c3')

node1.next, node2.next = node2, node6
node3.next, node4.next, node5.next = node4, node5, node6
node6.next, node7.next, node8.next = node7, node8, None

print(getIntersectionNode(node1, node3).val)

