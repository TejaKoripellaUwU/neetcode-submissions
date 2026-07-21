class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        class dset:
            def __init__(self):
                self.arr = [i for i in range(len(points))]
                self.rank = [0 for i in range(len(points))]

            def find(self,i):
                if i == self.arr[i]:
                    return i
                r = self.find(self.arr[i])
                self.arr[i] = r
                return r
            
            def add(self,u,v):
                p1 = self.find(u)
                p2 = self.find(v)
                if p1 == p2:
                    return False
                if self.rank[p1] > self.rank[p2]:
                    self.arr[p2] = p1
                elif self.rank[p2] > self.rank[p1]:
                    self.arr[p1] = p2
                else:
                    self.arr[p1] = p2
                    self.rank[p1] += 1
                return True
        edges = []
        v = set()
        for ind1,i in enumerate(points):
            for ind2,u in enumerate(points):
                if ind1 != ind2 and tuple(sorted([ind1,ind2])) not in v:
                    edges.append([abs(u[0]-i[0])+abs(u[1]-i[1]),ind1,ind2])
                    v.add(tuple(sorted([ind1,ind2])))
        edges = sorted(edges)
        res = 0
        d = dset()
        for c,u,v in edges:
            if d.add(u,v):
                res+=c            
        return res

        
