class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        x={}
        y={}
        for i in range(97,123):
            x[chr(i)]=0
            y[chr(i)]=-1
        k=0
        for i in s:
            x[i]+=1
            y[i]=k
            k+=1
        c=len(s)
        for i in x:
            if x[i]==1:
                c=min(y[i],c)
        if c==len(s):
            return -1
        return c
