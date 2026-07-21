class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [9999]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for val in coins:
                if i-val >= 0:
                    dp[i] = min(dp[i],dp[i-val]+1)
        print(dp)
        return -1 if dp[-1] == 9999 else dp[-1]