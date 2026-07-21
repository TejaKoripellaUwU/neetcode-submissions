class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = deque()
        for i in asteroids:
            if i>0:
                s.append(i)
            else:
                if s and s[-1] > 0:
                    while s and s[-1]>0 and abs(i)>s[-1]:
                        s.pop()

                    if s and s[-1]>0 and abs(i) == s[-1]:
                        s.pop()
                        continue
                if not s or s[-1] < 0:
                    s.append(i)

        return list(s)

