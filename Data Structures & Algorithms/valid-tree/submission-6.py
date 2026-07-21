class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        alist = defaultdict(set)
        visited = set()
        for i,j in edges:
            alist[i].add(j)
            alist[j].add(i)
        def dfs(node, prevNode):
            visited.add(node)
            for i in alist[node]:
                if i != prevNode:
                    if i not in visited:
                        dfs(i,node)
                    else:
                        return False
            return True
        return dfs(0,-1) and len(visited) == n
        
        

