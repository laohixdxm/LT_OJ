#firstBadVersion
#bug1,
#mid = (1+n)//2

#bug2, 
#def isBadVersion(version):
#    if(version>=2):
#        return False
#    else:
#        return True

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if(version>=2):
        return True
    else:
        return False


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while(start<end):

            mid = (start+end)//2
            print(start, end, mid)
            if(isBadVersion(mid)):
                end = mid 
            else:
                start = mid + 1

        if(start==end):
            return start
        else:
            print("...")  

s1 = Solution()
print(s1.firstBadVersion(4))
print(s1.firstBadVersion(5))
print(s1.firstBadVersion(6))



