#bug1, 
#TreeNode(-1) as empty tag to terminate DFS traversal
#if(parent.val == -1):
#    return visited

#bug2, 
#stack.append(parent) is missing after backtracing
#(CONT)as stack.pop previously, stack.append is necessary to backtrace the parent of the right child 
#stack.append(parent)
#node = parent.right

#bug3,
#if current node is left child of parent but right child of parent is null, 
#(CONT)backtrace just like current node is  right child of parent
#while(node == parent.right): =>
#while(node == parent.right) or ((node==parent.left) and (parent.right==None)):

graph1 = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

graph2 = {'A':['B', 'C'],
            'B':['D', 'E'],
            'C':['F', 'G'],
            'D':[], 'E':[], 'F':[], 'G':[],
}

graph3 = {'A':['B', 'C'],
            'B':[],
            'C':[]
}


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(graph, start, cnt, visited):
    print(start, cnt, end=" ")
    visited.append(start) 
    if(len(graph[start])==0):
        return

    for i in range(0, len(graph[start])):        
        dfs(graph, graph[start][i], cnt+1, visited)

    return visited


'''
def dfs2(graph, start, cnt, visited):
    #print(start, cnt, end=" ")
    #stack.append(start)

    node = start
    visited.append(emtpy tag)
    #for i in range(0, 2)):
    while node
        print(node)
        visited.append(node)

        if(node is leaf)
            parent = stack.pop()
            while(node == parent.right) 
                node = parent
                parent = stack.pop()
                if(parent != empty tag)
                     return       
            node = parent.right
        if(node has left)
            stack.push(node)
            node=node.left
        if(node only has right)
            stack.push(node)
            node=node.right
'''

def dfs2(root):
    node = root
    visited, stack = [], []
    stack.append(TreeNode(-1))
    #parent 

    while node:
        print(node.val)
        visited.append(node.val)
        #stack.append(node)

        if(node.left == None) and (node.right == None):
            parent = stack.pop()
            while(node == parent.right) or ((node==parent.left) and (parent.right==None)):
                node = parent
                parent = stack.pop()
                if(parent.val == -1):
                    print("-1-1")
                    return visited

            stack.append(parent)
            node = parent.right
            

            print("..", node, parent.val)
            #try:
            #    tmp=node.left
            #except:
            #    print(node, "...")

        elif(node.left != None):
            stack.append(node)
            node=node.left
        elif(node.left == None) and (node.right != None):
            stack.append(node)
            node=node.right

    #print("end")
    #return visited
    


#print(dfs(graph2, 'A', 1, visited=[])) 
#print(dfs(graph3, 'A', 1, visited=[])) 

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3

print(dfs2(node1), "***")

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
#node2.right = node5
node3.left = node6
node3.right = node7

print(dfs2(node1), "***")

#print(node2.right.val)





