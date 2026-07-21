class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        p1,p2 = 0,0
        while p1<len(s) and p2<len(s):
            tp1,tp2 = p1,p2
            while tp1>=0 and tp2<len(s) and s[tp1] == s[tp2]:
                res+=1
                tp1-=1
                tp2+=1
            if p1 == p2:
                p2+=1
            else:
                p1+=1
        return res