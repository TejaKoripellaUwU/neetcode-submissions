class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        elements = []
        for i in counts:
            heapq.heappush(elements,(-counts[i],i))
        pending = deque()
        t = 0
        while elements or pending:
            t += 1
            if pending and pending[0][1] < t:
                heapq.heappush(elements,pending[0][0])
                pending.popleft()
            
            if elements:
                cnt, ele = heapq.heappop(elements)
                if -cnt>1:
                    pending.append(((cnt+1, ele),t+n))
        return t



