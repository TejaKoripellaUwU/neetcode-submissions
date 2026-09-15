class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = [(-a,"a"),(-b,"b"),(-c,"c")]
        heapq.heapify(h)
        r = ""
        while h:
            f,l = heapq.heappop(h)
            f *= -1
            if f:
                if len(r) >= 2 and r[-1] == r[-2] == l:
                    if h:
                        f2,l2 = heapq.heappop(h)
                        if f2:
                            f2*=-1
                            r += l2
                            heapq.heappush(h,(-1*(f2-1),l2))
                    else:
                        return r
                else:
                    r+=l
                    f -= 1
                
                heapq.heappush(h,(-1*f,l))
        return r
