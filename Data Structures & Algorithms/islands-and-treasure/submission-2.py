from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2**31 -1
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited = set((i,j))
                    q = deque([(i,j,0)])
                    while q:
                        i,j,d = q.popleft()
                        for x,y in dirs:
                            ni,nj = i+x,j+y
                            if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj]>=0 and (ni,nj) not in visited:
                                grid[ni][nj] = min(grid[ni][nj],d+1)
                                q.append((ni,nj,d+1))
                                visited.add((ni,nj))
        
