from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        
        for index, i in enumerate(nums):
            target = -i
            arr = nums[:index] + nums[index+1:]
            seen = set()
            
            for j in arr:
                complement = target - j
                if complement in seen:
                    triplet = tuple(sorted([i, j, complement]))
                    res.add(triplet)
                seen.add(j)
        
        return [list(triplet) for triplet in res]
