class Solution:
    def get_tuple(self,a,matrix):
        return (a//len(matrix[0]), a%len(matrix[0]))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p1 = 0
        p2 = (len(matrix))*(len(matrix[0]))-1
        if len(matrix) == 1:
            p2 = (len(matrix))*(len(matrix[0])-1)
        if len(matrix[0]) == 1:
            p2 = (len(matrix)-1)*(len(matrix[0]))

        if len(matrix) == 1 and len(matrix[0])== 1:
            if matrix[0][0] == target:
                return True
            return False

        print(p1,p2)
        while p1<p2:
            split = (p2-p1)//2 + p1
            print(split)
            splitc = self.get_tuple(split,matrix)
            print(splitc)
            if target < matrix[splitc[0]][splitc[1]]:
                p2 = split-1
            elif target > matrix[splitc[0]][splitc[1]]:
                p1 = split + 1
            else:
                return True
        print("reached")
        p1c = self.get_tuple(p1,matrix)
        print(p1)
        print(p1c)
        if matrix[p1c[0]][p1c[1]] == target:
            return True
        else:
            return False
