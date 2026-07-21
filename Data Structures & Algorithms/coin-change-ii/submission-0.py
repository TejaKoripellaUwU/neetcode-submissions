class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for j in coins[::-1]:
            for i in range(1,len(dp)):
                if i-j>=0:
                    dp[i] += dp[i-j]
        return dp[-1]