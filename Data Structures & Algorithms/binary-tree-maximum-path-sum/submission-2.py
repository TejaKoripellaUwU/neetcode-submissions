# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        m = root.val
        def dfs(cur):
            nonlocal m
            if cur == None:
                return 0
            
            l = dfs(cur.left)
            r = dfs(cur.right)
            m = max(m,l+r+cur.val,cur.val+l,cur.val+r,cur.val)

            return max(cur.val+l,cur.val+r,cur.val)
        dfs(root)
        return m