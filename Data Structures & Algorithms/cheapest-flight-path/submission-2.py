class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra's over a graph with k*n nodes
        # let k = 3
        # node n,z will connect to neighbor(n),z+1 until z = k where all nodes will have no edges
        # end nodes will be (dst,z), (dst,z+1)... (dst,k)
        alist = defaultdict(list)
        for u,v,d in flights:
            for i in range(k+1):
                alist[(u,i)].append((d,(v,i+1)))
        q = [(0,(src,0))]
        v = set()
        # print(alist)
        while q:
            d,ele = heapq.heappop(q)
            # print(d,ele,q)
            if ele[0] == dst:
                return d

            if ele in v:
                continue
            v.add(ele)
            for d2,n in alist[ele]:
                heapq.heappush(q,(d2+d,n))

        return -1
