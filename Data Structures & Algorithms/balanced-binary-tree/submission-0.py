# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        m = [True]

        def get_height(node):
            if node == None:
                return 0

            r = get_height(node.right)
            l = get_height(node.left)

            if abs(r-l)>1:
                m[0] = False

            return max(r,l)+1
        
        if not root:
            return True

        get_height(root)

        return m[0]