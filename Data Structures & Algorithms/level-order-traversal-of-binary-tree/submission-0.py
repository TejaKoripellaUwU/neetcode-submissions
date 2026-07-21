# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        res = [[]]
        queue.append((root,0))
        while len(queue)>0:
            ele = queue.pop()
            if len(res) <= ele[1]:
                res.append([])

            res[ele[1]].append(ele[0].val)
            if ele[0].right:
                queue.append((ele[0].right,ele[1]+1))
            if ele[0].left:
                queue.append((ele[0].left,ele[1]+1))
        
        return res



        