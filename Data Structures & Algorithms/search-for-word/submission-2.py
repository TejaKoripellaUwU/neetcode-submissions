class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,c,prev):
            if c>=len(word):
                return True
            
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            for x,y in directions:
                n,t = x+i, y+j
                if ((n,t) not in prev):
                    if 0<=n<len(board) and 0<=t<len(board[0]) and board[n][t] == word[c]:
                        prev.add((i,j))
                        if dfs(n,t,c+1,prev):
                            return True
                        prev.remove((i,j))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    print("reached")
                    if dfs(i,j,1,set()):
                        return True
        return False