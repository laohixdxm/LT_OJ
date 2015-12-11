#[DP] Invert Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def IsLeaf(self, node):
        return (node!=None) and (node.left==None) and (node.right==None)

    def ex(self, root):
        left = root.left
        root.left = root.right
        root.right = left

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """        
        if(root==None) or self.IsLeaf(root):
            return root

        self.ex(root)
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


def CreateTree(NodeList):
    for i in range(0,len(NodeList)):
        if(NodeList[i]==None):
            continue    
        if(2*i+1<len(NodeList)):
            NodeList[i].left = NodeList[2*i+1]
        if(2*i+2<len(NodeList)):
            NodeList[i].right = NodeList[2*i+2]
    return NodeList[0]


def print_node(node):
    if(node==None):
        print("None")
    else:
        print(node.val)


def bfs(root): #could not handle internal layer(not lowest layer) node is None
    fifo=[]
    fifo.append(root)
    while(len(fifo)>0):
        node = fifo.pop(0)
        print_node(node)
        if(node==None):
            #fifo.append(None)
            #fifo.append(None)
            continue
        fifo.append(node.left)
        fifo.append(node.right)

# [4,2,7,1,3,6,9]
NodeList1 = [TreeNode(4), TreeNode(2), TreeNode(7)]
NodeList1.extend([TreeNode(1), TreeNode(3), TreeNode(6), TreeNode(9)])
root1 = CreateTree(NodeList1)

s1 = Solution()
root2 = s1.invertTree(root1)
bfs(root2) #[4,7,2,9,6,3,1]






