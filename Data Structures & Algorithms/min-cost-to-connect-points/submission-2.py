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
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges = sorted(edges)
        res = 0
        d = dset()
        added = 0
        for c,u,v in edges:
            if added == len(points):
                break
            if d.add(u,v):
                res+=c
                added+=1         
        return res

        
