class Solution:
    def integerBreak(self, n: int) -> int:
        # unbounded knapsack
        # dp[2..n] where dp[i] is the max product of i
        dp = [-999 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(n+1):
            for j in range(i):
                dp[i] = max(dp[i], max(i-j,dp[i-j])*j)
        return dp[-1]