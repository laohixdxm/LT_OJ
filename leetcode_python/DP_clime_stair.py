#[dynamic programming] climbe stairs, initial version

#You are climbing a stair case. It takes n steps to reach to the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if((n==1)or(n==0)):
            return 1
        elif(n>=2):
            return self.climbStairs(n-1) + self.climbStairs(n-2)

s1=Solution()
print(s1.climbStairs(1))
print(s1.climbStairs(2))
print(s1.climbStairs(3))


