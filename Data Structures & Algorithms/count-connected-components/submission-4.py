class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d=defaultdict(set)
        v = set()
        for i in edges:
            d[i[0]].add(i[1])
            d[i[1]].add(i[0])
        for i in range(n):
            v.add(i)
        c = 0

        while v:
            q = [v.pop()]
            while q:
                ele = q.pop(0)
                print(v)
                for i in d[ele]:
                    if i in v:
                        v.remove(i)
                        q.append(i)
            c+=1
        return c

        