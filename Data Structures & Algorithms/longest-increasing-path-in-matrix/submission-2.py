class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[-1]*len(matrix[0]) for i in range(len(matrix))]
        def dfs(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            dirs = [[0,1],[1,0],[-1,0],[0,-1]]
            dp[i][j] = 1
            for x,y in dirs:
                n_x = x+i
                n_y = y+j
                # print(n_x,n_y)
                if n_x>=0 and n_x<len(matrix) and n_y>=0 and n_y<len(matrix[i]) and matrix[n_x][n_y] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(n_x,n_y)+1)
            
            return dp[i][j]
        m = 1
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j] == -1:
                    dfs(i,j)
                m = max(m,dp[i][j])
        print(dp)
        return m
        
            
            
