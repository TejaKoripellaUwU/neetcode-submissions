class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        valid = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    valid.add((i,j))
        res = 0
        if not valid:
            return res
        q = deque([valid.pop()])
        while valid or q:
            while q:
                i,j = q.popleft()
                print(i,j,res,valid)
                dirs = [[0,1],[1,0],[-1,0],[0,-1]]
                for x,y in dirs:
                    if (i+x,j+y) in valid and 0<= i+x < len(grid) and 0<= j+y < len(grid[0]):
                        q.append((i+x,j+y))
                        valid.remove((i+x,j+y))

            res+=1
            if valid:
                q = deque([valid.pop()])
        return res            