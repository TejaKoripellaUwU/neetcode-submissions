class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mi = prices[0]
        for i in prices:
            if i<mi:
                mi = i
            else:
                res = max(res,i-mi)
        return res