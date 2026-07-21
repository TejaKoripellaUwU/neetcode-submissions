from typing import List
from collections import defaultdict, Counter

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(s,ind):
            if ind >= len(nums) and s == target:
                return [[]]
            if ind >= len(nums):
                return []
            if s > target:
                return []
            
            res = []
            res.extend(dfs(s,ind+1))

            out = dfs(s+nums[ind],ind)
            for i in out:
                i.append(nums[ind])
            res.extend(out)
            return res

        return dfs(0,0)
            


