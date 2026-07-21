class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(s,t):
            if len(t) == 0:
                return 1
            
            res = 0
            if s:
                if s[0] == t[0]:
                    res += dfs(s[1:],t[1:])
                res += dfs(s[1:],t)
            return res
        
        return dfs(s,t)