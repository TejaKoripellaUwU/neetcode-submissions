class Solution:
    def s(self,l):
        # print(l[1])
        return l[1]
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedpos = list(enumerate(position))
        sortedpos.sort(reverse = True, key = self.s)
        # # print(list(enumerate(position)))
        # print(sortedpos)
        q = deque()
        for i in sortedpos:
            if len(q) != 0:
                ts = float(target - q[-1][0])/q[-1][1]
                cs = float(target - i[1])/speed[i[0]]
                print(ts)
                print(cs)
                if ts<cs:
                    q.append((i[1],speed[i[0]]))
            else:
                q.append((i[1],speed[i[0]]))
        return len(q)