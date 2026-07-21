class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        depth = sum(nums)
        if (depth%2) != 0:
            return False
        dp = [[False]*len(nums) for _ in range(depth+1)]
        off = int(depth/2)
        for i in range(len(nums)):
            if i == 0:
                dp[off+nums[i]][0] = True
                dp[off-nums[i]][0] = True
                continue
            for j in range(depth):
                if j+nums[i]<depth:
                    dp[j][i] = max(dp[j+nums[i]][i-1],dp[j][i])
                if j-nums[i]>=0:
                    dp[j][i] = max(dp[j-nums[i]][i-1],dp[j][i])
        return dp[off][-1]