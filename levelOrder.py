# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans,level=[],[root]
        b=[]
        while root and level:
            ans.extend([node.val for node in level])
            b.append(ans)
            ans=[]
            level=[kid for n in level for kid in (n.left, n.right) if kid]
        return b
