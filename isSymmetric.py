# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        x=[]
        y=[]
        val_x=[]
        val_y=[]
        if root.left:
            x+=[root.left]
            val_x+=[root.val]
        if root.right:
            y+=[root.right]
            val_y+=[root.val]
        m=[]
        n=[]
        while len(x) and len(y):
            p=x.pop()
            q=y.pop()
            if p:
                val_x+=[p.val]
                m+=[p.left,p.right]
            else:
                val_x+=[-1111]
            if q:
                val_y+=[q.val]
                n+=[q.right,q.left]
            else:
                val_y+=[-1111]
            if len(x)==len(y)==0:
                x=m
                y=n
                m=[]
                n=[]
        return val_x==val_y and len(x)==len(y)
