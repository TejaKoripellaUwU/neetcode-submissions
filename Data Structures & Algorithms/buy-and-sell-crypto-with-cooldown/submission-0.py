class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def recur(i,coin):
            if i >= len(prices):
                return 0
            r1 = 0
            if not coin:
                r1 = max(recur(i+1,1) - prices[i],r1)
            else:
                r1 = max(recur(i+2,0) + prices[i],r1)
            
            r1 = max(recur(i+1,coin), r1)

            return r1
        
        return recur(0,0)