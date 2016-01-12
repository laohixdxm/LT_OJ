#leetcode, BestTimeBuySell, initial version, has bug
#fix bug, list out of range

import pdb

def max_price(prices, start, end, max_arr):
    #pdb.set_trace()
    if(start == end):
        #min_arr[start] = prices[start]
        return prices[start]

    #print(start)
    if(max_arr[start] == None):
        max_arr[start] = \
            max_price(prices, start+1, end, max_arr)
    return max_arr[start]


def maxProfit(prices):
    diff = 0
    max_arr = [None]*len(prices)

    for i in range(len(prices)-1):
        buy = prices[i]
        sell = max_price(prices, i+1, len(prices)-1, max_arr)
        cur_diff = sell - buy
        if(cur_diff > diff):
            diff = cur_diff
    return diff


prices_arr = [1,2,3]
print(maxProfit(prices_arr)) 


