from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ch = set()
        p1 = 0
        p2 = 1
        m = 1
        ch.add(s[p1])
        while p2 < len(s):
            if s[p2] in ch:
                ch.remove(s[p1])
                p1+=1
            else:
                if (p2-p1+1)>m:
                    m = p2-p1+1
                ch.add(s[p2])
                p2+=1
                
        return m
                