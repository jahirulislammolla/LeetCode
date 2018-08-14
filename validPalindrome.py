class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x=''
        y=''
        j=len(s)-1
        c=0
        for i in range(len(s)):
            if s[i]!=s[j]:
                x=s[i+1:j+1]
                y=s[i:j]
                break
            j-=1
        c1=0
        c2=0
        j=len(x)-1
        for i in range(len(x)):
            if x[i]==x[j]:
                c1+=1
            if y[i]==y[j]:
                c2+=1
            j-=1
        return c1==len(x) or c2==len(x)
