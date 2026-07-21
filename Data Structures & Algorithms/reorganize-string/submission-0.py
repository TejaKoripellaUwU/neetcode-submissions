class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)
        h = []
        for k,v in d.items():
            heapq.heappush(h,(-v,k))
        res = ""
        hold = None
        while h:
            v,k = heapq.heappop(h)
            v+=1
            res += k
            if hold:
                heapq.heappush(h,hold)
                hold = None
            if v != 0:
                hold = (v,k)
        return res if not hold else ""
            