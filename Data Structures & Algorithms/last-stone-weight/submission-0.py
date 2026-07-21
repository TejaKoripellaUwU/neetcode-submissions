import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for i in stones:
            heapq.heappush(h,-i)

        while len(h) > 1:
            r1 = heapq.heappop(h)
            r2 = heapq.heappop(h)
            res = (-r1) - (-r2)
            if res != 0:
                heapq.heappush(h,-abs(res))
        if len(h) == 1:
            return abs(h[0])
        else:
            return 0
