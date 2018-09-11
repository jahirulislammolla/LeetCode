class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=1
        while l<=len(s)//2:
            p=s[:l]
            ck=0
            for i in range(0,len(s)-l+1,l):
                if s[i:i+l]==p:
                    
                    continue
                else:
                    ck=1
                    break
            l+=1
            if ck==0 and len(s)%len(p)==0:
                return True
        return False
