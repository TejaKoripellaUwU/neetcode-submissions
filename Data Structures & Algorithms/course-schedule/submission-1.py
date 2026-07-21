class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        v = set()
        t = set()
        g = defaultdict(list)
        for i in prerequisites:
            g[i[0]].append(i[1])
        
        print(g)
        def dfs(cur):
            v.add(cur)
            for i in g[cur]:
                if i in t:
                    continue
                if i not in v:
                    if not dfs(i):
                        return False
                else:
                    return False
            v.remove(cur)
            t.add(cur)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            v = set()
            
        return True

                
            
            