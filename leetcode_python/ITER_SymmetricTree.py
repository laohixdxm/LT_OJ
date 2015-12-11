#symmetric tree, iterative

#bug record "node.left" mistaken as "node.right": 
#if(node.left!=None): fifo.append(node.right)
#=> if(node.right!=None): fifo.append(node.right)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isLayerSym(self, fifo):
        #for i,j in zip(range(len(fifo), range(len(), 0, -1)):
        for i in range(len(fifo)):
            j = len(fifo)-1-i
            if(fifo[i]==fifo[j]==None):
                continue
            elif(fifo[i]!=None) and (fifo[j]!=None) and (fifo[i].val==fifo[j].val):
                continue
            else:
                print(i,j)
                print(fifo[0].val)
                print(fifo[3].val)
                return False

        return True

    def print_fifo(self, fifo):
        for i in range(0,len(fifo)):
            if(fifo[i]==None):
                print(fifo[i], end=" ")
            else:                
                print(fifo[i].val, end=" ")
        print()

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        fifo = []
        fifo.append(root)
        while len(fifo)>0:
            print("len", len(fifo))
            self.print_fifo(fifo)
            #for i in range(0,len(fifo)):
            #    print("val", fifo[i].val)

            if(not self.isLayerSym(fifo)):
                return False
            for i in range(0, len(fifo)):
                node = fifo.pop(0)
                if(node==None):
                    continue
                if(node.left!=None):
                    fifo.append(node.left)
                else:
                    fifo.append(None)
                if(node.right!=None):
                    fifo.append(node.right)
                else:
                    fifo.append(None)

        return True


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node1.left = node2
node1.right = node3
s1 = Solution()
print(s1.isSymmetric(node1))

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
#node5 = TreeNode(5)
#node5 = TreeNode('#')
node5 = None
#node6 = TreeNode(5)
#node6 = TreeNode('#')
node6 = None
node7 = TreeNode(3)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

s1 = Solution()
print(s1.isSymmetric(node1))

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
#node5 = TreeNode(5)
#node5 = TreeNode('#')
node5 = None
#node6 = TreeNode(5)
#node6 = TreeNode('#')
node6 = TreeNode(5)
node7 = TreeNode(3)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

s1 = Solution()
print(s1.isSymmetric(node1))



