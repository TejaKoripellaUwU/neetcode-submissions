class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        p1 = 0
        p2 = len(arr)

        while (p1 < p2):
            m = (p1+p2)//2
            if (x > arr[m]):
                p1 = m+1
            else:
                p2 = m
        l = p1-1
        r = p1

        res = deque([])
        for i in range(k):
            c = (arr[l] if 0 <= l < len(arr) else -10000000, arr[r] if 0 <= r < len(arr) else -10000000)
            if abs(c[0] - x) <= abs(c[1]-x):
                res.appendleft(c[0])
                l -= 1
            else:
                res.append(c[1])
                r += 1
        return list(res)


