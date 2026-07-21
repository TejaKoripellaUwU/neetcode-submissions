class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        walls = deque([])
        for i in height:
            tmp_ele = []
            while walls and i>walls[-1]:
                tmp_ele.append(walls.pop())
            if not walls and tmp_ele:
                wat_h = min(tmp_ele.pop(),i)
                for j in range(len(tmp_ele)):
                    total += wat_h - tmp_ele[j]
            elif walls:
                wat_h = i
                for j in range(len(tmp_ele)):
                    total += wat_h - tmp_ele[j]
                    walls.append(wat_h)
            else:
                walls.append(i)
                continue
            walls.append(i)
            # print(i,total,wat_h,walls)
        return total