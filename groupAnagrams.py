class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        x={}
        for i in strs:
            m="".join(sorted(i))
            if m not in x:
                x[m]=[]
            x[m]+=[i]
        n=[]
        for i in x:
            n+=[x[i]]
        return n
