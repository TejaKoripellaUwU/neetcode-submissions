class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0]*(len(stoneValue)+3)
        for i in range(len(stoneValue)-1,-1,-1):
            add = stoneValue[i]
            dp[i] = add-dp[i+1]
            for j in range(2,4):
                if i+j <= len(stoneValue):
                    add+=stoneValue[i+j-1]
                    dp[i] = max(dp[i],add-dp[i+j])
        print(dp)
        if dp[0] == 0:
            return "Tie"
        if dp[0] > 0:
            return "Alice"
        return "Bob"