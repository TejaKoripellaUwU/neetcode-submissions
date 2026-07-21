class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != (len(s1)+len(s2)):
            return False
        if not len(s1):
            return s2 == s3
        if not len(s2):
            return s1 == s3

        dp = [[False]*(len(s2)+1) for i in range(len(s1)+1)]
        
        dp[len(dp)-1][len(dp[0])-1] = True
        
        for i in range(len(dp)-1,-1,-1):
            for j in range(len(dp[0])-1,-1,-1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                    continue
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True

        return dp[0][0]
        # def recur(p1,p2):
        #     if p1 == len(s1) and p2 == len(s2):
        #         return True
            
        #     if p1<len(s1) and s1[p1] == s3[p1+p2]:
        #         if recur(p1+1,p2):
        #             return True
            
        #     if p2<len(s2) and s2[p2] == s3[p1+p2]:
        #         if recur(p1,p2+1):
        #             return True
            
        #     return False
        # return recur(0,0)