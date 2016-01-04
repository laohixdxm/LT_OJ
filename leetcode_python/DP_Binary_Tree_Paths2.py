#[DP] Binary Tree Paths 

<<<<<<< HEAD
#["1->2->5", "1->3"]
   
#pseudo prototype
def binaryTreePaths_core0(self, root, stack, list_arg):
    if(self.IsLeaf(root)):
        for i in range(len(stack)):
            f(stack[i])
        f(root)
        list_arg.append(str1)
        return
=======
#["1->2->5", "1->3"]        
#pseudo prototype
def binaryTreePaths_core0(self, root, stack, list_arg):
    if(self.IsLeaf(root)):
    for i in range(len(stack)):
        f(stack[i])
    f(root)
    list_arg.append(str1)
    return
>>>>>>> dd5c16da6f775770ca0c8debb2bc44fd599efe50

    stack.append(root.val)

    self.binaryTreePaths_core(root.left, stack, list_arg)
    self.binaryTreePaths_core(root.right, stack, list_arg)

<<<<<<< HEAD
    stack.pop()
=======
    stack.pop()    stack.append(root.val)
>>>>>>> dd5c16da6f775770ca0c8debb2bc44fd599efe50
    return


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def IsLeaf(self, node):
        return (node!=None) and (node.left==None) and (node.right==None)


    def binaryTreePaths_core(self, root, stack, list_arg):
        str1=""
        if(self.IsLeaf(root)):
            for i in range(len(stack)):
                #print(stack[i], end=" ")
                str1 = str1 + str(stack[i]) + "=>"
            str1 += str(root.val)
            print(str1)
            list_arg.append(str1)
            return

        if(root == None):
            return

        stack.append(root.val)

        self.binaryTreePaths_core(root.left, stack, list_arg)
        self.binaryTreePaths_core(root.right, stack, list_arg)

        stack.pop()
        return


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        stack = []
        res_list1 = []
        self.binaryTreePaths_core(root, stack, res_list1)
        return res_list1


def CreateTree(NodeList):
    for i in range(0,len(NodeList)):
        if(NodeList[i]==None):
            continue    
        if(2*i+1<len(NodeList)):
            NodeList[i].left = NodeList[2*i+1]
        if(2*i+2<len(NodeList)):
            NodeList[i].right = NodeList[2*i+2]
    return NodeList[0]


NodeList1 = [TreeNode(1), TreeNode(2), TreeNode(3)]
NodeList1.extend([None, TreeNode(5), None, None])
root1 = CreateTree(NodeList1)

s1 = Solution()
print(s1.binaryTreePaths(root1)) 





