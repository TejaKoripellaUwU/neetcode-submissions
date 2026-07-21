class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            mi = 100000000
            for j in range(i,-1,-1):
                mi = min(heights[j],mi)
                res = max(res,mi*(i-j+1))
        return res