class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self):
                self.arr = [i for i in range(len(edges))]
                self.rank = [1 for i in range(len(edges))]
                print(self.arr)
            
            def find(self,i):
                if self.arr[i] == i:
                    return i
                self.arr[i] = self.find(self.arr[i])
                return self.arr[i]

            def merge_cycle(self,i,j):
                i = self.find(i)
                j = self.find(j)
                if i == j:
                    return True
                else:
                    if self.rank[i] == self.rank[j]:
                        self.rank[j]+=1
                        self.arr[i] = j
                    elif self.rank[i] > self.rank[j]:
                        self.arr[j] = i
                    else:
                        self.arr[i] = j
                    return False
        
        uf = UnionFind()
        for i,j in edges:
            if uf.merge_cycle(i-1,j-1):
                return [i,j]
