class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        
        last_m = 0
        while queue:
            i,j,m = queue.popleft()
            directions = [[1,0],[0,-1],[-1,0],[0,1]]
            last_m = max(last_m,m)
            for x,y in directions:
                if len(grid)>x+i>=0 and len(grid[0])>y+j>=0 and grid[x+i][y+j] == 1:
                    grid[x+i][y+j] = 2
                    queue.append((x+i,y+j,m+1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return last_m
        
                