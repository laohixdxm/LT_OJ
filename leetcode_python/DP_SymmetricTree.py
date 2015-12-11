#[DP] Symmetric Tree

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def cmp(self, left, right):
        if(left==right==None):
            return True
        if(left==None) and (right!=None): 
            return False
        if(left!=None) and (right==None): 
            return False
        if(left != None) and (right != None):
            if(left.val != right.val):
                return False

        return self.cmp(left.left, right.right) and self.cmp(left.right, right.left)


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.cmp(root.left, root.right)


#list1 = {1,2,2}
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node1.right = node2
node1.left = node3
s1 = Solution()
print(s1.isSymmetric(node1))


#{1,2,2,3,4,4,3}
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(3)
node7 = TreeNode(3)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

s1 = Solution()
print(s1.isSymmetric(node1))



