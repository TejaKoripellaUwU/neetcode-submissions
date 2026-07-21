class Solution:
    def solve(self, board: List[List[str]]) -> None:
        os = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    os.add((i,j))
        # print((8,9) in os)
        if os:
            while os:
                failed = False
                ele = os.pop()
                v = {ele}
                q = [ele]
                os.add(ele)
                while q:
                    e = q.pop()
                    # print(e in os)
                    if e == (8,9):
                        print(v)
                        print("reaccghed")
                    if e in os:
                        os.remove(e)
                    # print(e[0],e[1])
                    if e[0] == 0 or e[1] == 0 or e[0] == len(board)-1 or e[1] == len(board[0])-1:
                        failed = True
                        break

                    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
                    for x,y in dirs:
                        if (e[0]+x,e[1]+y) not in v and board[e[0]+x][e[1]+y] == "O":
                            v.add((e[0]+x,e[1]+y))
                            q.append((e[0]+x,e[1]+y))
                # print("comp")
                if not failed:
                    for i,j in v:
                        board[i][j] = "X"            
                         
            
            