#leetcode, Binary Search Tree Lowest Common Ancestor 
#small trick for multiple () in one line 

import pdb

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    list1, list2 = [], []

#    list1.append(root)
    node = root
    while(p.val !=  node.val):
        list1.append(node)
        if(p.val < node.val):
            node = node.left
        elif(p.val > node.val):
            node = node.right
#        list1.append(node)
    list1.append(node)

#    list2.append(root)
    node = root
    while(q.val !=  node.val):
        list2.append(node)
        if(q.val < node.val):
            node = node.left
        elif(q.val > node.val):
            node = node.right
#        list2.append(node)
    list2.append(node)

    print(len(list1), len(list2))
    #pdb.set_trace()
    #return
    #for i in range(min(len(list1), len(list2))):
    for i in range(2):
        if(list1[i] == list2[i]):
            continue
        else:
            i -= 1
            break
    #pdb.set_trace()
    return list1[i]

node1, node2, node3 = TreeNode(6), TreeNode(2), TreeNode(8)
node4, node5, node6, node7 = TreeNode(0), TreeNode(4), TreeNode(7), TreeNode(9)
node10, node11 = TreeNode(3), TreeNode(5)

node1.left, node1.right = node2, node3
(node2.left, node2.right), (node3.left, node3.right) = (node4, node5), \
    (node6, node7)
node5.left, node5.right = node10, node11

print(lowestCommonAncestor(node1, node2, node3).val)
print(lowestCommonAncestor(node1, node2, node5).val)




