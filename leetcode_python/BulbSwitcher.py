#leetcode BulbSwitcher

import pdb

def toggle(bulb):
    if(bulb==0):
        bulb = 1
    elif(bulb==1):
        bulb = 0
    return bulb


def bulbSwitch(n):
    bulbs = [0,0,0]
    for i in range(n):
        #print(i)
        bulbs[i] = 0

    times = 1
    while(times<=n):
        for i in range(times-1, n, times):
            bulbs[i] = toggle(bulbs[i])

        #pdb.set_trace()
        times+=1

    cnt=0
    for i in range(n):
        if(bulbs[i]==1):
            cnt+=1
    return cnt

print(bulbSwitch(3))
