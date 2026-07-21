class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[0])-2,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i+1][j+1]+1,dp[i][j])
                dp[i][j] = max(dp[i][j+1],dp[i][j])
                dp[i][j] = max(dp[i+1][j],dp[i][j])

        return dp[0][0]


        # def recur(s1,s2):
        #     if len(s1) == 0 or len(s2) == 0:
        #         return 0
            
        #     r = 0
        #     if s1[0] == s2[0]:
        #         r = max(r,recur(s1[1:],s2[1:])+1)
        #     r = max(r,recur(s1[1:],s2))
        #     r = max(r,recur(s1,s2[1:]))

        #     return r
        
        # return recur(text1,text2)

