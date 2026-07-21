class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        def dfs(s,ind,skip):
            if s == target:
                return [[]]
            if ind>= len(candidates) or s > target:
                return []
            if candidates[ind] == candidates[ind-1] and skip:
                return dfs(s,ind+1,True)

            
            res = []
            out = dfs(s+candidates[ind],ind+1,False)
            for i in out:
                i.append(candidates[ind])
            res.extend(out)
            res.extend(dfs(s,ind+1,True))
            return res

        r = dfs(0,0,False)
        # for i in range(len(r)):
        #     r[i] = tuple(r[i])

        # r = list(set(r))
        # for i in range(len(r)):
        #     r[i] = list(r[i])

        return r


