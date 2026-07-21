# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m=[0]

        def get_height(node):
            if node == None:
                return 0

            r = get_height(node.right)
            l = get_height(node.left)

            print(r+l)

            if m[0] < r+l:
                m[0]= r+l

            return max(r,l)+1
        
        if not root:
            return 0

        get_height(root)
        return m[0]
        

        
        