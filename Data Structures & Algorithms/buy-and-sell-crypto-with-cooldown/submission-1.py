class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [[0]*3 for _ in range(len(prices)+2)]

        for i in range(len(dp)-3,-1,-1):
            for j in range(2,-1,-1):
                if j == 1:
                    dp[i][j] = max(dp[i+2][0]+prices[i],dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][1]-prices[i],dp[i][j])

                dp[i][j] = max(dp[i+1][j],dp[i][j])
        
        return dp[0][0]

        # def recur(i,coin):
        #     if i >= len(prices):
        #         return 0
        #     r1 = 0
        #     if not coin:
        #         r1 = max(recur(i+1,1) - prices[i],r1)
        #     else:
        #         r1 = max(recur(i+2,0) + prices[i],r1)
            
        #     r1 = max(recur(i+1,coin), r1)

        #     return r1
        
        # return recur(0,0)