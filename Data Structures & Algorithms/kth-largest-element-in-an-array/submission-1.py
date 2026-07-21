class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in nums:
            heapq.heappush_max(h,i)
        
        res = 0
        for j in range(k):
            res = heapq.heappop_max(h)
        return int(res)