#Binary Tree Level Order Traversal, actually BFS (Breadth First Search)

#pseudo
def levelOrder0(self, root):
    fifo = []
    fifo.append(root)
    while 1:#while ?
        layer=[]
        for i in range(len(fifo)):
            node = fifo.pop(0)
            fifo.append(node.left)
            fifo.append(node.right)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res_list = []
        fifo=[]
        fifo.append(root)
        while(len(fifo)>0):
            layer=[]
            for i in range(len(fifo)):
                node=fifo.pop(0)
                if(node.left!=None):
                    fifo.append(node.left)
                if(node.right!=None):
                    fifo.append(node.right)

                layer.append(node.val)
            res_list.append(layer)
        return res_list


def CreateTree(NodeList):
    for i in range(0,len(NodeList)):
        if(NodeList[i]==None):
            continue
        if(2*i+1<len(NodeList)):
            NodeList[i].left = NodeList[2*i+1]
        if(2*i+2<len(NodeList)):
            NodeList[i].right = NodeList[2*i+2]
    return NodeList[0]


#{3,9,20,#,#,15,7}
NodeList1 = [TreeNode(3), TreeNode(9), TreeNode(20)]
NodeList1.extend([None, None, TreeNode(15), TreeNode(7)])
#NodeList1.extend([TreeNode(4), TreeNode(5), None, TreeNode(7)])
root1 = CreateTree(NodeList1)

s1 = Solution()
print(s1.levelOrder(root1))



