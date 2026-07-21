class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self):
                self.arr = [i for i in range(len(edges))]
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
                    self.arr[i] = j
                    return False
        
        uf = UnionFind()
        for i,j in edges:
            if uf.merge_cycle(i-1,j-1):
                return [i,j]
