class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        def dfs(s,ind):
            if s == target:
                return [[]]
            if ind>= len(candidates) or s > target:
                return []

            
            res = []
            out = dfs(s+candidates[ind],ind+1)
            for i in out:
                i.append(candidates[ind])
            res.extend(out)
            res.extend(dfs(s,ind+1))
            return res

        r = dfs(0,0)
        for i in range(len(r)):
            r[i] = tuple(r[i])

        r = list(set(r))
        for i in range(len(r)):
            r[i] = list(r[i])

        return r


