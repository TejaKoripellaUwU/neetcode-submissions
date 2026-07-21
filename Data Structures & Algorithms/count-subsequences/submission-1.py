class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s)+1) for i in range(len(t)+1)]
        for j in range(len(dp[0])):
            dp[-1][j] = 1
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[0])-2,-1,-1):
                if s[j] == t[i]:
                    dp[i][j] += dp[i+1][j+1]
                dp[i][j] += dp[i][j+1]
        return dp[0][0]
        # def dfs(s,t):
        #     if len(t) == 0:
        #         return 1
            
        #     res = 0
        #     if s:
        #         if s[0] == t[0]:
        #             res += dfs(s[1:],t[1:])
        #         res += dfs(s[1:],t)
        #     return res
        
        # return dfs(s,t)