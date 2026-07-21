class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = defaultdict(list)
        for i in prerequisites:
            m[i[0]].append(i[1])

        visited = set()
        visiting = set()
        res = []

        def dfs(cur):
            if cur in visited:
                return True
            if cur in visiting:
                return False

            visiting.add(cur)
            print(cur,visiting,visited,res)
            for i in m[cur]:
                print(i)
                if not dfs(i):
                    return False

            res.append(cur)
            visiting.remove(cur)
            visited.add(cur)
            return True

        for i in range(numCourses):
            if not dfs(i):
                print("failed")
                return []
        return res
        