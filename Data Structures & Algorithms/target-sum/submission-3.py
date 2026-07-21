class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target)>s:
            return 0
        dp = [[0]*((2*s)+1) for i in range(len(nums)+1)]
        dp[0][s] = 1

        for i in range(1,len(dp)):
            for j in range(-s,s+1):
                if (j+nums[i-1])<=s:
                    dp[i][j+s] += dp[i-1][j+nums[i-1]+s]

                if (j-nums[i-1])>=-s:
                    dp[i][j+s] += dp[i-1][j-nums[i-1]+s]
        print(dp)
        return dp[-1][target+s]