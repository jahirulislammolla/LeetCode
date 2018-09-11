class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=s.split(" ")
        c=0
        for i in x:
            if i!='':
                c+=1
        return c
