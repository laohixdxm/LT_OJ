#[DP] Unique BST, 

#bug1,
#indention error for "total = left+right"
#bug2,
#    elif(len(set0)==0):
#        return 0
#bug3,
#total = left+right

'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

def numTrees(set0, cnt):
    #print(set0)    
    if(len(set0)==1):
        return 1
    elif(len(set0)==0):
        return 1

    total=left=right=mul=0

    for i in set0:
        set1=set()
        set2=set()
        for j in set0:
            if(j<i):
                set1.add(j)
                #total+=numTrees(set1)
            elif(j>i):
                set2.add(j)
                #total+=numTrees(set2)    
        left=numTrees(set1, cnt+1)
        right=numTrees(set2, cnt+1)    
        #if(cnt==1):
        #    print("tota1", total1, i)
        #    print("tota2", total2, i)
        #    print(i)
        #total+=total1
        #total+=total2
        mul = left * right
        total += mul
    return total


set0 = set()
for i in range(1, 3+1):
    #print(i)
    set0.add(i)
    
#print(numTrees(set0))

print(numTrees({1,2,3}, 1))
print(numTrees({2,3}, 1))
print(numTrees({1,2}, 1))
print(numTrees({1}, 1))
