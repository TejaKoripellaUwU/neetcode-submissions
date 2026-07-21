class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for i in s]
        res = 0
        for j in range(len(dp)):
            for i in range(len(dp)):
                if i>j:
                    dp[i][j] = True
                elif i == j:
                    dp[i][j] = True
                    res+=1
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res+=1
                else:
                    dp[i][j] = False
        # print(dp)
        return res
                