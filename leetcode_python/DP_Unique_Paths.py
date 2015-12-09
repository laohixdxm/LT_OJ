#[dynamic programming] Unique Paths

#bug1: without wrap function, m and n of m*n grid both should be minus 1
#bug2: if(y==0): return x elif(x==0) return y 


'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

def f(y, x):
    if(y==0):
        return 1#return f(0,n-1)
    elif(x==0):
        return 1#return f(m-1,0)
    return f(y-1,x) + f(y,x-1)

def wrap(m, n):
    return f(m-1, n-1)


print(wrap(2, 2))
print(wrap(2, 3))
print(wrap(3, 3))
print(wrap(3, 7))
