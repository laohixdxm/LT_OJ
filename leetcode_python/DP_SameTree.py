#[DP] Same Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def IsLeaf(self, node):
        return (node!=None) and (node.left==None) and (node.right==None)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if(p==q==None): #base case
            return True
        elif(self.IsLeaf(p) and self.IsLeaf(q) and (p.val==q.val)): #base case
            return True
        elif((p!=None) and (q!=None)and (p.val==q.val)): # root pass vertification, go recursion
            pass
        else: #fail, then terminate
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def CreateTree(NodeList):
    for i in range(0,len(NodeList)):
        if(2*i+1<len(NodeList)):
            NodeList[i].left = NodeList[2*i+1]
        if(2*i+2<len(NodeList)):
            NodeList[i].right = NodeList[2*i+2]
    return NodeList[0]


s1 = Solution()
root1 = CreateTree([TreeNode(1), TreeNode(2), TreeNode(3)])
root2 = CreateTree([TreeNode(1), TreeNode(2), TreeNode(3)])
print(s1.isSameTree(root1, root2))

NodeList1 = [TreeNode(1), TreeNode(2), TreeNode(3)]
NodeList1.extend([TreeNode(4), TreeNode(5), None, TreeNode(7)])
NodeList2 = [TreeNode(1), TreeNode(2), TreeNode(3)]
NodeList2.extend([TreeNode(4), TreeNode(5), None, TreeNode(7)])
#print(NodeList)
root1 = CreateTree(NodeList1)
root2 = CreateTree(NodeList2)
print(s1.isSameTree(root1, root2))









