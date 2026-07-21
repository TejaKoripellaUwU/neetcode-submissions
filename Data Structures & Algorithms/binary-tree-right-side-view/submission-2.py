# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def dfs(node):
            if node == None:
                return None

            r = dfs(node.right)
            l = dfs(node.left)
            print(r,l)
            if not r and not l:
                print("reached")
                return [node.val]
            if not r:
                l.insert(0,node.val)
                return l
            if not l:
                r.insert(0,node.val)
                return r
            if len(l)>len(r):
                r.insert(0,node.val)
                r.extend(l[len(r)-1:])
            else:
                r.insert(0,node.val)
            return r
        
        return dfs(root)

    
        