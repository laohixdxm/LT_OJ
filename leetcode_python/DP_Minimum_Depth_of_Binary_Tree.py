#[DP] Minimum Depth of Binary Tree, inital version

#[DP] Minimum Depth of Binary Tree, inital version
#bug: [1,2] => 1 (expected: 2)

#bug: [1,2] => 1 (expected: 2)
#fix [1,2] => 1 bug, by help function MinOfSubDepth


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def IsLeaf(self, node):
        return (node!=None) and (node.left==None) and (node.right==None)

    def MinOfSubDepth(self, root):
        if(root.left!=None)and(root.right!=None)
        :
            return min(self.minDepth(root.left), self.minDepth(root.right))
        elif(root.left!=None)and(root.right==None):
            return self.minDepth(root.left)
        elif(root.left==None)and(root.right!=None):
            return self.minDepth(root.right)


    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root==None):
            return 0
        elif(self.IsLeaf(root)):
            return 1
        return 1 + self.MinOfSubDepth(root) 


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
print(s1.minDepth(root1))

NodeList1 = [TreeNode(3), TreeNode(9), None]
root1 = CreateTree(NodeList1)

s1 = Solution()
print(s1.minDepth(root1))

