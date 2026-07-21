class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        alist = defaultdict(list)
        for i,j in edges:
            alist[i].append(j)
            alist[j].append(i)
        
        visited = set()
        res = 0
        for i in range(n):
            q = deque([])
            if i in visited:
                continue
            q.append(i)
            visited.add(i)
            while q:
                e = q.popleft()
                for j in alist[e]:
                    if j not in visited:
                        q.append(j)
                        visited.add(j)
            res+=1
        return res