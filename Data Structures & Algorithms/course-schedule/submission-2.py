class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(set)
        inver = [0]*numCourses
        for cur,pre in prerequisites:
            adj_list[pre].add(cur)
            inver[cur] += 1
        
        q = deque([])
        for i in range(numCourses):
            if inver[i] == 0:
                q.append(i)

        while q:
            k = q.popleft()
            for i in adj_list[k]:
                inver[i] -= 1
                if inver[i] == 0:
                    q.append(i)
        
        for i in inver:
            if i != 0:
                return False
        return True

