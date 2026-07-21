class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def check_palindrome(s):
            return s.reverse() == s

        def backtrack(cur,ind):
            if ind >= len(s):
                res.append(cur.copy())
                return
            
            for j in range(ind,len(s)):
                if s[ind:j+1][::-1] == s[ind:j+1]:
                    cur.append(s[ind:j+1])
                    backtrack(cur,j+1)
                    cur.pop(-1)
            return
        backtrack([],0)
        return res