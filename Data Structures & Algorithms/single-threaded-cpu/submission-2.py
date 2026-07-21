class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        q1 = []
        res = []
        for ind,i in enumerate(tasks):
            tasks[ind] = (i[0],i[1],ind)
        tasks = deque(sorted(tasks))
        print(tasks)
        t = tasks[0][0]
        print(t)
        while tasks or q1:
            while tasks and tasks[0][0] <= t:
                ele = tasks.popleft()
                heapq.heappush(q1,ele[1:])
            if q1:
                res.append(q1[0][1])
                t += heapq.heappop(q1)[0]
            else:
                ele = tasks.popleft()
                heapq.heappush(q1,ele[1:])
                t = ele[0]

        return res
