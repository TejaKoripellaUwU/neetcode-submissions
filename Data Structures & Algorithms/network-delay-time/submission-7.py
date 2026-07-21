class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * n
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((w,v))
        dist[k-1] = 0
        q = deque([k])
        while q:
            e = q.popleft()
            for w,v in adj[e]:
                if dist[v-1] > dist[e-1]+w:
                    dist[v-1] = dist[e-1]+w
                    q.append(v)
        r = max(dist)
        # print(dist)
        return r if r<float("inf") else -1

        # for _ in range(n - 1):
        #     for u, v, w in times:
        #         if dist[u - 1] + w < dist[v - 1]:
        #             dist[v - 1] = dist[u - 1] + w
        # max_dist = max(dist)
        # return max_dist if max_dist < float('inf') else -1