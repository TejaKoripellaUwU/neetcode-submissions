class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        land = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land.add((i,j))
        if not land:
            return 0
        res = 1
        q = deque([land.pop()])
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        while land:
            csize = 0
            while q:
                i,j = q.pop()
                csize += 1
                for x,y in dirs:
                    if 0 <= i+x < len(grid) and 0 <= j+y < len(grid[0]) and (i+x,j+y) in land:
                        q.append((i+x,j+y))
                        land.remove((i+x,j+y))
            if land:
                q.append(land.pop())
            res = max(res,csize)
        return res
                