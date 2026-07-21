# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = dict()
        for i in range(len(preorder)):
            m[inorder[i]] = i
        
        def dfs(p1,p2, val):
            if p1 >= p2:
                return None

            split = m[preorder[val]]
            # for split in range(p1,p2):
            #     if inorder[split] == preorder[val]:
            #         break
            res = TreeNode(preorder[val])
            pre = (p1,split)
            post = (split+1,p2)

            res.left = dfs(pre[0],pre[1],val+1)
            res.right = dfs(post[0],post[1],val+pre[1]-pre[0]+1)

            return res

        return dfs(0,len(preorder),0)
             