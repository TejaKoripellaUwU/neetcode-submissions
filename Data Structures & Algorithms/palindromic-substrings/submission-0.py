class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        for i in range(len(s)):
            p1,p2 = i,i
            while p1>=0 and p2<len(s) and s[p1] == s[p2]:
                res.append(s[p1:p2+1])
                p1 -= 1
                p2 += 1
            if i<len(s)-1:
                p1,p2 = i,i+1
                while  p1>=0 and p2<len(s) and s[p1] == s[p2]:
                    res.append(s[p1:p2+1])
                    p1 -= 1
                    p2 += 1
        print(res)
        return len(res)
