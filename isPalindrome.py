class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x!=0 and x%10==0):
            return False
        x=list(str(x))
        return x==x[::-1]
