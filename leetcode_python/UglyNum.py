#ugly number, initial version
#fix bug, print(s1.isUgly(0)) suspend

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num<=0):
            return False
        while((num%2==0)or(num%3==0)or(num%5==0)):
            if(num%2==0):
                num=num/2
            elif(num%3==0):
                num=num/3
            elif(num%5==0):
                num=num/5
        if(num==1):
            return True
        else:
            return False

s1 = Solution()
print(s1.isUgly(14))
print(s1.isUgly(6))
print(s1.isUgly(8))
print(s1.isUgly(0))