class Solution:
    def isPalindrome(self, m):
        """
        :type s: str
        :rtype: bool
        """
        s=''
        t=''
        for i in m:
            i=i.lower()
            if "a"<=i<="z" or '0'<=i<='9':
                s+=i
                t=i+t
        return s==t
                
