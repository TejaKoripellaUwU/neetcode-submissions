class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            cur_min = 1000000
            width = 0
            for j in range(i,len(heights)):
                cur_min = min(heights[j],cur_min)
                width += 1
                res = max(res, width*cur_min)
        return res