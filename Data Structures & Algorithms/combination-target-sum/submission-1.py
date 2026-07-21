from typing import List
from collections import defaultdict, Counter

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        memo = {}

        def dfs(targ):
            if targ in memo:
                return memo[targ]
            if targ == 0:
                return [()]
                
            res = set()
            for num in nums:
                if targ - num >= 0:
                    for path in dfs(targ - num):
                        new_path = tuple(sorted(path + (num,)))
                        res.add(new_path)
            memo[targ] = res
            return res

        result_tuples = dfs(target)
        return [list(tup) for tup in result_tuples]
