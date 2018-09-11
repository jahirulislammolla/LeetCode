# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        x={}
        ma=0
        m=[]
        if root:
            m+=[root.left, root.right]
            x[root.val]=1
            ma=1
        while len(m)>0:
            p=m.pop()
            if p:
                m+=[p.left,p.right]
                if p.val not in x:
                    x[p.val]=0
                x[p.val]+=1
                if x[p.val]>ma:
                    ma=x[p.val]
        y=[]
        for i in x:
            if x[i]==ma:
                y+=[i]
        return sorted(y)
