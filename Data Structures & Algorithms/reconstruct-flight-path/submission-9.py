class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u,v in tickets:
            adj[u].append(v)
        for k,v in adj.items():
            adj[k] = sorted(adj[k])
        res = []
        def dfs(cur):
            res.append(cur)
            if len(res) == len(tickets)+1:
                return True
            for ind,ele in enumerate(adj[cur]):
                adj[cur].pop(ind)
                if dfs(ele):
                    return True
                adj[cur].insert(ind,ele)
            res.pop(-1)
            return False
        dfs("JFK")
        return res
                