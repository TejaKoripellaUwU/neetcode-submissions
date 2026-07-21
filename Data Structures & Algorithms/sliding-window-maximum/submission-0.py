class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i+k <= len(nums):
                m = -100000
                for j in range(i,i+k):
                    m = max(m,nums[j])
                res.append(m)
        return res
            