class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p0 = 0
        p1 = 0
        res = 0
        cs = set()
        while p0 < len(s) and p1 < len(s):
            if s[p1] not in cs:
                cs.add(s[p1])
                p1 += 1
                res = max(len(cs),res)
            else:
                cs.remove(s[p0])
                p0 += 1
        return res