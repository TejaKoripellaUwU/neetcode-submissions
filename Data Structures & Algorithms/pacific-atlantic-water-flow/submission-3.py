from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h = len(heights)
        w = len(heights[0])
        pac_o = set()
        atl_o = set()
        for i in range(h):
            pac_o.add((i,0))
            atl_o.add((i,w-1))
        for i in range(w):
            pac_o.add((0,i))
            atl_o.add((h-1,i))
        q = list(pac_o)
        while q:
            y,u = q.pop(0)
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]
            for i in dirs:
                r,p = i
                if 0<y+r<h and 0<u+p<w and heights[y+r][u+p]>=heights[y][u] and (y+r,u+p) not in pac_o:
                    pac_o.add((y+r,u+p))
                    q.append((y+r,u+p))

        b = list(atl_o)
        while b:
            y,u = b.pop(0)
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]
            for i in dirs:
                r,p = i
                if 0<=y+r<h and 0<=u+p<w and heights[y+r][u+p]>=heights[y][u] and (y+r,u+p) not in atl_o:
                    atl_o.add((y+r,u+p))
                    b.append((y+r,u+p))
        print(pac_o)
        print(atl_o)
        return list(pac_o.intersection(atl_o))
        
        


