#leetcode, Binary Tree Level Order TraversalII

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrderBottom(root):
    """
    :type root:TreeNode
    :rtype: List[List[int]]
    """
    fifo = []
    layers = []
    res = []
    fifo.append(root)
    while(len(fifo)>0):
        layer = []
        for i in range(len(fifo)):
            cur = fifo.pop(0)
            print(cur.val)
            if(cur.left!=None):
                fifo.append(cur.left)
            if(cur.right!=None):
                fifo.append(cur.right)
            layer.append(cur.val)
        layers.append(layer)
    for i in range(len(layers)):
        res.append(layers.pop())

    return res

node1, node2, node3 = TreeNode(3), TreeNode(9), TreeNode(20)
node6, node7 = TreeNode(15), TreeNode(7)
node1.left, node1.right = node2, node3
node3.left, node3.right = node6, node7
print(levelOrderBottom(node1))















