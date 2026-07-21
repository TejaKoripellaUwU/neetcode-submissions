import copy

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best = 10000000000
        while l<=r:
            mid = (l+r)//2
            s = self.sim(piles,mid)
            # print(s,mid)
            if (s>h):
                l = mid + 1
            elif (s<=h):
                if mid<best:
                    best = mid
                r = mid - 1

        return best

    
    def sim(self, piles,size):
        t = 0
        for i in piles:
            t += math.ceil(i/size)
        return t

