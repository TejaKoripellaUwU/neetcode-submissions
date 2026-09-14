# 123456
# TTTTTT

# 345612
# FFFFTT

# FT

class Solution:
    def findMin(self, nums: List[int]) -> int:
        p1 = 0
        p2 = len(nums)
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        while p1 < p2:
            m = (p1+p2)//2
            if nums[m] < nums[0]:
                p2 = m
            else:
                p1 = m + 1
        return nums[p1] 

        
