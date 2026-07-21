class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q = deque([(i, j)])
                    grid[i][j] = 0
                    area = 0

                    while q:
                        r, c = q.popleft()
                        area += 1

                        for dr, dc in dirs:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                q.append((nr, nc))
                                grid[nr][nc] = 0

                    res = max(res, area)

        return res