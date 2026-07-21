import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        p_heap = []
        heapq.heapify(p_heap)
        for i in points:
            heapq.heappush(p_heap,(math.sqrt(i[0]**2+i[1]**2),i))
        res = []
        for i in range(k):
            res.append(heapq.heappop(p_heap)[1])
        return res
