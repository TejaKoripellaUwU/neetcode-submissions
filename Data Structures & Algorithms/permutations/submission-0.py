class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        def dfs(cur,remaining):
            if not remaining:
                final.append(cur.copy())
                return
            
            for i in range(len(remaining)):
                cur.append(remaining[i])
                dfs(cur,remaining[:i]+remaining[i+1:])
                cur.pop(-1)
            return
        dfs([],nums)
        return final