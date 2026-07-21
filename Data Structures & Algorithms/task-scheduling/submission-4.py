class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        elements = []
        for i in counts:
            heapq.heappush(elements,(-counts[i],i))
        pending = []
        t = 0
        while elements or pending:
            t += 1
            opt1 = None
            opt2 = None
            if pending and (pending[0][0]+n) < t:
                ot,cnts,ele = pending[0]
                opt1 = (t,cnts-1,ele)


            if elements:
                cnts, ele = elements[0]
                cnts = -cnts
                opt2 = (t,cnts-1,ele)

            if opt1 and opt2:
                if opt2[1] > opt1[1]:
                    heapq.heappop(elements)
                    if opt2[1]>0:
                        heapq.heappush(pending,opt2)
                else:
                    heapq.heappop(pending)
                    if opt1[1]>0:
                        heapq.heappush(pending,opt1)
                continue
            if opt1:
                heapq.heappop(pending)
                if opt1[1]>0:
                    heapq.heappush(pending,opt1)
            elif opt2:
                heapq.heappop(elements)
                if opt2[1]>0:
                    heapq.heappush(pending,opt2)    

        return t



