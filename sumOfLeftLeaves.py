# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s=0
        m=[root]
        while m:
            p=m.pop()
            if p==None:
                continue
            if p.left:
                if p.left.left==None and p.left.right==None:
                    s+=p.left.val
                m+=[p.left]
            if p.right:
                m+=[p.right]
        return s
