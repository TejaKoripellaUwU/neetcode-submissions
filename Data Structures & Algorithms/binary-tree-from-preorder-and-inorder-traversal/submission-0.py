# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(arr, val):
            # print(val,arr)
            if not arr:
                return None

            split = 0
            for split in range(len(arr)):
                if arr[split] == preorder[val]:
                    break
            # print(split)
            res = TreeNode(preorder[val])
            pre = arr[:split]
            post = arr[split+1:]

            res.left = dfs(pre,val+1)
            res.right = dfs(post,val+len(pre)+1)

            return res

        return dfs(inorder,0)
             