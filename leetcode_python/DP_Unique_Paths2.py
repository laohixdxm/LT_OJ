#[DP] Unique Paths2, inital version

'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.
'''

def f(y,x, obstacleGrid):
  """
  type y: int
  type x: int
  type obstacleGrid: List[List[int]]
  rtype: int
  """
  if(obstacleGrid[y][x]==1):
    return 0

  if(y==0) or (x==0):
    return 1
  else:
    return f(y-1,x, obstacleGrid) + f(y,x-1, obstacleGrid)


def wrap(m,n, obstacleGrid):
  """
  type m: int
  type n: int
  type obstacleGrid: List[List[int]]
  rtype: int
  """
  return f(m-1,n-1, obstacleGrid)

list1 = [0,0,0]
list2 = [0,1,0]
list3 = [0,0,0]

list_2D = [list1, list2, list3]
print(wrap(3,3,list_2D))

list1 = [0,0,0,0]
list2 = [0,1,0,0]
list3 = [0,0,0,0]
list_2D = [list1, list2, list3]
print(wrap(3,4,list_2D))





