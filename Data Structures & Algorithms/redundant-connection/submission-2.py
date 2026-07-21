class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        v = {edges[0][0]}
        def dfs(node, his):
            for i in d[node]:
                if his and i == his[-1][0]:
                   continue
                elif i in v:
                    his.append([node,i])
                    return his
                else:
                    v.add(i)
                    his.append([node,i])
                    res = dfs(i,his)
                    if res:
                        return res
                    his.pop(-1)
        matches = dfs(edges[0][0],[])
        res = set()
        for ind in range(len(matches)):
            res.add(frozenset(matches[ind]))

        print(res,matches)
        for ind, i in enumerate(edges[::-1]):
            print(i)
            if frozenset(i) in res:
                return edges[len(edges)-1-ind]



        
        