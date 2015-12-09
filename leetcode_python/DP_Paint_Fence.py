'''
Problem Description:

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
'''

#def paint_core(NumColor, start, end):
#    Return paint_core()



#def paint(NumPost, NumColor):
#    paint_core(NumColor, 0, NumPost-1)

def f(n, k):
    if(n<3):
        return pow(k, n)
    return k*(f(n-1, k) - 1)

print(f(2,1))
print(f(1,5))

print(f(2,3))
print(f(3,4))

#print(pow(5,2))





