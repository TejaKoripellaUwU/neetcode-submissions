import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        for u, v, w in times:
            d[u].append((w, v))
            
        pq = [(0, k)]
        
        min_dist = {}
        
        max_time = 0
        
        while pq:
            time, node = heapq.heappop(pq)
            
            if node in min_dist:
                continue
            
            min_dist[node] = time
            max_time = max(max_time, time)
            
            for weight, neighbor in d[node]:
                if neighbor not in min_dist:
                    heapq.heappush(pq, (time + weight, neighbor))
                    
        return max_time if len(min_dist) == n else -1
