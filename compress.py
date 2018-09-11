class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        c=0
        m=[]
        p=chars[0]
        for i in chars:
            if p==i:
                c+=1
            else:
                if c>1:
                    m+=[p]
                    m+=list(str(c))
                else:
                    m+=[p]
                c=1
                p=i
        if c>1:
            m+=[p]
            m+=list(str(c))
        if c==1:
            m+=[p]
        c=0
        for i in m:
            if c<len(chars):
                chars[c]=i
            else:
                chars.append(i)
            c+=1
        return c
