class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    q = deque([(i,j)])
                    grid[i][j] = "0"
                    while q:
                        i,j = q.pop()
                        for x,y in dirs:
                            ni,nj = i+x,j+y
                            if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj] == "1":
                                q.append((ni,nj))
                                grid[ni][nj] = "0"
                    res += 1
        return res