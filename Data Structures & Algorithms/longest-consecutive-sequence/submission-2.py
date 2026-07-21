class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0
        while s:
            oc = s.pop()
            c = oc
            cl = 1
            while c+1 in s:
                s.remove(c+1)
                cl+=1
                c += 1
            c = oc
            while c-1 in s:
                s.remove(c-1)
                cl += 1
                c -= 1
            l = max(cl,l)
        return l