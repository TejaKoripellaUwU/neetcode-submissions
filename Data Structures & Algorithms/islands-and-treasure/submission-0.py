class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        height = len(grid)
        width = len(grid[0])
        z = []
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    z.append((i,j))

        for i in z:
            v = set()
            q = [(i,0)]
            dr = [(1,0),(0,1),(-1,0),(0,-1)]
            while q:
                cell,dist = q.pop(0)
                v.add(cell)
                ele = grid[cell[0]][cell[1]]
                grid[cell[0]][cell[1]] = min(dist,ele)
                for j in dr:
                    # print(cell[0]+j[0] >= 0 and cell[0]+j[0] < height and cell[1]+j[1] >= 0 and cell[1]+j[1] < width and grid[cell[0]+j[0]][cell[1]+j[1]] != -1)
                    if cell[0]+j[0] >= 0 and cell[0]+j[0] < height and cell[1]+j[1] >= 0 and cell[1]+j[1] < width and grid[cell[0]+j[0]][cell[1]+j[1]] != -1 and (cell[0]+j[0],cell[1]+j[1]) not in v:
                        q.append(((cell[0]+j[0],cell[1]+j[1]),dist+1))



