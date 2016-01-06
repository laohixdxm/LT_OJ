#leetcode BalancedBST

def depth(root):
    if(root==None):
        return 0
    else:
        return 1 + max(depth(root.left), depth(root.right))

def isBanlanced(root):
    depth1 = depth(root.left)
    depth2 = depth(root.right)
    if(max(depth1,depth2) - min(depth1, depth2) > 1):
        return False
    else:
        return True

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node1, node2, node3 = TreeNode(1), TreeNode(2), TreeNode(3)
node1.left, node1.right = node2, node3
print(isBanlanced(node1)) 


node1, node2, node4, node5 = TreeNode(1), TreeNode(2), TreeNode(4), TreeNode(5)
node1.left, node1.right = node2, None
node1.right = TreeNode(3)

node2.left, node2.right = node4, node5
print(isBanlanced(node1)) 






