class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited_pacific = set()
        visited_atlantic = set()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0:
                    visited_pacific.add((i,j))
                if j == 0:
                    visited_pacific.add((i,j))
                if i == len(heights)-1:
                    visited_atlantic.add((i,j))
                if j == len(heights[0])-1:
                    visited_atlantic.add((i,j))
        
        q_pac = deque(list(visited_pacific))
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        while q_pac:
            i,j = q_pac.popleft()
            for x,y in dirs:
                if 0 <= i+x < len(heights) and 0 <= j+y < len(heights[0]) and (i+x,j+y) not in visited_pacific and heights[i+x][j+y] >= heights[i][j]:
                    visited_pacific.add((i+x,j+y))
                    q_pac.append((i+x,j+y))
        
        q_atl = deque(list(visited_atlantic))
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        while q_atl:
            i,j = q_atl.popleft()
            for x,y in dirs:
                if 0 <= i+x < len(heights) and 0 <= j+y < len(heights[0]) and (i+x,j+y) not in visited_atlantic and heights[i+x][j+y] >= heights[i][j]:
                    visited_atlantic.add((i+x,j+y))
                    q_atl.append((i+x,j+y))
        
        targ = visited_atlantic.intersection(visited_pacific)
        res = []
        for i in targ:
            res.append(list(i))
        return res