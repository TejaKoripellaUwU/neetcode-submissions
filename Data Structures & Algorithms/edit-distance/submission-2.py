class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[100000]*(len(word1)+1) for i in range(len(word2)+1)]

        for i in range(len(dp)-1,-1,-1):
            for j in range(len(dp[0])-1,-1,-1):
                if i == len(dp)-1 and j == len(dp[0])-1:
                    dp[i][j] = 0
                    continue

                if i<len(dp)-1 and j<len(dp[0])-1 and word2[i] == word1[j]:
                    dp[i][j] = dp[i+1][j+1]
                    continue
                
                if i == len(dp)-1:
                    dp[i][j] = dp[i][j+1]+1
                    continue

                if j == len(dp[0])-1:
                    dp[i][j] = dp[i+1][j]+1
                    continue
                
                dp[i][j] = min(dp[i][j],dp[i+1][j]+1,dp[i+1][j+1]+1,dp[i][j+1]+1)

        return dp[0][0]
        # def dfs(w1,w2):
        #     if w1 == "" and w2 == "":
        #         return 0

        #     if w1 and w2 and w1[0] == w2[0]:
        #         return dfs(w1[1:],w2[1:])
            
        #     if not w1:
        #         return dfs(w1,w2[1:])+1
            
        #     if not w2:
        #         return dfs(w1[1:],w2)+1
            
        #     res = dfs(w1[1:],w2)+1
        #     res = min(res, dfs(w1,w2[1:])+1)
        #     res = min(res, dfs(w1[1:],w2[1:])+1)

        #     return res
        
        # return dfs(word1,word2)