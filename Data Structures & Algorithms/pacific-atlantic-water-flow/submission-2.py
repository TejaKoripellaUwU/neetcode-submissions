from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h = len(heights)
        w = len(heights[0])
        pac_o = set()
        atl_o = set()

        # Pacific: top and left borders
        for i in range(h):
            pac_o.add((i,0))
            atl_o.add((i,w-1))
        for j in range(w):
            pac_o.add((0,j))
            atl_o.add((h-1,j))

        def bfs(start_set):
            visited = set(start_set)
            q = list(start_set)
            while q:
                y, x = q.pop(0)
                for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w:
                        if heights[ny][nx] >= heights[y][x] and (ny, nx) not in visited:
                            visited.add((ny, nx))
                            q.append((ny, nx))
            return visited

        pac_reach = bfs(pac_o)
        atl_reach = bfs(atl_o)

        return list(pac_reach & atl_reach)
