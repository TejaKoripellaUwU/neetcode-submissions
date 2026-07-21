class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        alist = defaultdict(list)
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        v = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                v[(i,j)] = 99999999
                for x,y in dirs:
                    ni,nj = x+i,y+j
                    if 0<=ni<len(grid) and 0<=nj<len(grid[0]):
                        alist[(i,j)].append((ni,nj))
        q = [(grid[0][0],(0,0))]
        
        while q:
            # print(q)
            p,u = heapq.heappop(q)
            for x,y in dirs:
                # print(u)
                ni,nj = x+u[0],y+u[1] 
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and v[(ni,nj)] > max(p,grid[ni][nj]):
                    heapq.heappush(q,(max(p,grid[ni][nj]),(ni,nj)))
                    v[(ni,nj)] = max(p,grid[ni][nj])
        # print(v)
        return v[(len(grid)-1,len(grid[0])-1)]
