class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def compare(w1,w2):
            p = 0
            for i in range(min(len(w1),len(w2))):
                if w1[i] != w2[i]:
                    return (w1[i],w2[i])
            
            if i == len(w1)-1:
                #Case that w1 is a prefix of w2
                return (0,0)
            # Case that w2 is a prefix of w1 (no solution)
            return (-1,-1)
        alist = defaultdict(list)
        indegree = defaultdict(int)
        allchars = set()
        for i in range(len(words)-1):
            res = compare(words[i],words[i+1])
            if res[0] == 0:
                continue
            if res[0] == -1:
                return ""
            alist[res[0]].append(res[1])
            indegree[res[1]]+=1
        for i in words:
            for j in i:
                allchars.add(j)
        
        q = []
        for k,v in alist.items():
            if indegree[k] == 0:
                heapq.heappush(q,(0,k))
        res = ""
        while q:
            deg,u = heapq.heappop(q)
            allchars.remove(u)
            res += u
            for v in alist[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    heapq.heappush(q,(0,v))
        # cycle detected
        if len(res) < len(alist.items()):
            return ""
        for i in allchars:
            res+=i
        return res
        
        