class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        memo = {}
        def search(targ:int,cur:tuple):
            if (targ,cur) in memo:
                return memo[(targ,cur)]
            if targ == 0:
                return [()]
            res = set()
            for ind,i in enumerate(cur):
                if targ-i>=0:
                    for path in search(targ-i, cur[:ind] + cur[ind + 1:]):
                        res.add(tuple(sorted(path+(i,))))
            memo[(targ,cur)] = res
            return res
        return [list(i) for i in search(target,tuple(candidates))]
