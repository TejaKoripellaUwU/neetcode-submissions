from copy import deepcopy
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ma = defaultdict(set)

        for i in edges:
            ma[i[0]].add(i[1])
            ma[i[1]].add(i[0])

        v = set()
        if not edges:
            return True
        q = [(edges[0][0],0)]
        while len(q)>0:
            print(q,ma)
            ele,prev = q.pop(0)
            v.add(ele)

            for i in ma[ele]:
                if i == prev and ele != prev:
                    continue
                if i in v:
                    return False
                else:
                    q.append((i,ele))


        return len(v) == n        
        
        