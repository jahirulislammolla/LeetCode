class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j=0
        if s=='':
            return True
        for i in range(len(t)):
            if t[i]==s[j]:
                j+=1
            if j==len(s):
                return True
        return False
