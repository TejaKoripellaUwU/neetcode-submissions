class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        alist = defaultdict(set)
        visited = set()
        for i,j in edges:
            alist[i].add(j)
            alist[j].add(i)
        def dfs(node):
            visited.add(node)
            for i in alist[node]:
                if i not in visited:
                    alist[i].remove(node)
                    dfs(i)
                else:
                    return False
            return True
        print(visited)
        return dfs(0) and len(visited) == n
        
        

