class Solution:
    def numSquares(self, n: int) -> int:
        # find smallest sum of perfect squares to n
        # dp[1...n] where dp[i] is smallest sum of perfect square to add to i
        # dp[i] = for p in perfectsqaures: dp[i] = min(dp[i-p]+1,dp[i])
        dp = [10000]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1,n+1):
            m = math.floor(math.sqrt(i)) #largest possible sqrt possible for this index
            print(i,m)
            for j in range(1,m+1):
                dp[i] = min(dp[i-(j**2)]+1,dp[i])
        print(dp)
        return dp[-1]