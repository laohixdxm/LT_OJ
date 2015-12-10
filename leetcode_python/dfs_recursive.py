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

        elif(node.left != None):
            stack.append(node)
            node=node.left
        elif(node.left == None) and (node.right != None):
            stack.append(node)
            node=node.right


print(dfs(graph2, 'A', 1, visited=[])) 
print(dfs(graph3, 'A', 1, visited=[])) 






