#CreateTree helper function for Tree related problem, tested by BFS

#fix bug for internal node(node in internal layer)is None, add None node processing
#        if(NodeList[i]==None):
#            continue    

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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


def bfs(root):
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


root1 = CreateTree([TreeNode(1), TreeNode(2), TreeNode(3)])
bfs(root1)

NodeList = [TreeNode(1), TreeNode(2), TreeNode(3)]
NodeList.extend([TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)])
#print(NodeList)
root1 = CreateTree(NodeList)
bfs(root1)



#{1,#,2,3}
#{1,2,3,#,#,4,#,#,5}

