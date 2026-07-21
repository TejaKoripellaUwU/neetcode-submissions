class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = dict()
        alist = defaultdict(list)
        for i in range(1,n+1):
            res[i] = -1
        for s,d,t in times:
            alist[s].append((t,d))
        pqueue = [(0,k)]
        res[k] = 0
        v = set()
        while pqueue:
            t1,s1 = heapq.heappop(pqueue)
            v.add(s1)
            for t2,s2 in alist[s1]:
                if res[s2] == -1 or t2+t1 < res[s2]:
                    heapq.heappush(pqueue,(t2+t1,s2))
                    res[s2]=t2+t1
        r = -1
        if len(v) != n:
            return -1
        for k,v in res.items():
            r = max(r,v)
        return r
