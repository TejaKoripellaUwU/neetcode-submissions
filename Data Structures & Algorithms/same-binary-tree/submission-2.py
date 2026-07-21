# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        m = []
        m1 = []
        def get_height1(node):
            if node == None:
                m.append(-500000000000000000000000)
                return 0
            l = get_height1(node.left)
            r = get_height1(node.right)
            if l:
                m.append(l.val)
            if r:
                m.append(r.val)
            m.append(node.val)
            return node

        def get_height2(node):
            if node == None:
                m1.append(-500000000000000000000000)
                return 0
            l = get_height2(node.left)
            r = get_height2(node.right)
            if l:
                m1.append(l.val)
            if r:
                m1.append(r.val)
            m1.append(node.val)
            return node
        
        

        get_height1(p)
        get_height2(q)
        if len(m1) != len(m):
            return False
        for ind,i in enumerate(m):
            if i != m1[ind]:
                return False

        return True 
        