#house robber initial version

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of 
money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have 
security system connected and (it will automatically contact the police if two adjacent houses were broken 
into on the same night).

Given a list of non-negative integers representing the amount of money of each house, determine the maximum 
amount of money you can rob tonight (without alerting the police).
'''

class Solution(object):
    def __init__ (self, nums):
        self.tmp = []
        for i in range(len(nums)+1):
            self.tmp.append([])
            for j in range(len(nums)+1):
                self.tmp[i].append(-1)


    def rob_core(self, nums, start, end, cnt):
        print("rob_core:start end cnt", start, end, cnt)
        max_total=0;
        cur_total=0

        if(self.tmp[start][end]!=-1):
            return self.tmp[start][end]

        if(start==end):
            self.tmp[start][start] = nums[start]
            return nums[start]            
        for i in range(start, end+1):
            #print("i:", i)
            if(i-2>=start)and(i+2<=end):
                cur_total = nums[i] + self.rob_core(nums, start, i-2, cnt+1) + self.rob_core(nums, i+2, end, cnt+1)
            elif(i-2>=start):
                cur_total = nums[i] + self.rob_core(nums, start, i-2, cnt+1)
            elif(i+2<=end):
                cur_total = nums[i] + self.rob_core(nums, i+2, end, cnt+1)
            else:
                cur_total = nums[i]
            if(cur_total>max_total):
                max_total=cur_total

        self.tmp[start][end] = max_total
        return max_total


    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #size = len(nums)
        #tmp[size][size]
        return self.rob_core(nums, 0, len(nums)-1, 1)

nums = [1,2,3,4,5,6,7]
s1= Solution(nums)
#import pdb
#pdb.set_trace()
res = s1.rob(nums) 
print(res)

nums = [6,3,10,8,2,10,3,5,10,5,3]
s2= Solution(nums)
res = s2.rob(nums) 
print(res)

#[2,1] => 2
nums = [2,1]
s2 = Solution(nums)
print(s2.rob(nums))

#[2,1,1,2] => 4
nums = [2,1,1,2]
s2 = Solution(nums)
print(s2.rob(nums))


















