class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(s1,s2,ci):
            if s1 == s2:
                return True
            if ci >= len(nums):
                return False

            return dfs(s1+nums[ci],s2-nums[ci],ci+1) or dfs(s1,s2,ci+1)
        
        return dfs(0,sum(nums),0)