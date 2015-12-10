import time

graph1 = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


graph2 = {'A':['B', 'C'],
            'B':['D', 'E'],
            'C':[],
            'D':[],
            'E':[],
}


def bfs(graph, start):
    arr = {'A':11,'B':22,'C':33,'D':44,'E':55, 'F':66}

    visited, stack = [], [start]

    while stack:
        vertex = stack.pop(0)
        if vertex not in visited:
            visited.extend(vertex)
            arr[vertex]=-1

            for i in range(0, len(graph[vertex])):
                if(arr[graph[vertex][i]] != -1):
                    stack.extend(graph[vertex][i])
                    print("stack", stack, "visited", visited)

    return visited


print(bfs(graph2, 'A')) 
print(bfs(graph1, 'A'))     