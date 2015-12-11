#[DP] PathSum

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def IsLeaf(self, node):
        return (node!=None) and (node.left==None) and (node.right==None)

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """        
        if(sum<0) or (root==None):
            return False
        elif(self.IsLeaf(root)):
            if(root.val==sum):
                return True
            else:
                return False

        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


def CreateTree(NodeList):
    for i in range(0,len(NodeList)):
        if(NodeList[i]==None):
            continue
        if(2*i+1<len(NodeList)):
            NodeList[i].left = NodeList[2*i+1]
        if(2*i+2<len(NodeList)):
            NodeList[i].right = NodeList[2*i+2]
    return NodeList[0]


NodeList1 = [TreeNode(1), None, TreeNode(3)]
NodeList1.extend([None, None, None, TreeNode(7)])
#NodeList1.extend([TreeNode(4), TreeNode(5), None, TreeNode(7)])
root1 = CreateTree(NodeList1)

s1 = Solution()
print(s1.hasPathSum(root1, 11))

NodeList1 = [TreeNode(5), TreeNode(4), TreeNode(8)]
NodeList1.extend([TreeNode(11), None, TreeNode(13), TreeNode(4)])
NodeList1.extend([TreeNode(7), TreeNode(2), None, None, None, None, None, TreeNode(1)])

root1 = CreateTree(NodeList1)

s1 = Solution()
print(s1.hasPathSum(root1, 22))


