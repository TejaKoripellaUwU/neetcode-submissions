class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = Counter(s)
        t = set()
        res = [0]
        ci = 0
        for i in s:
            d[i]-=1
            t.add(i)
            if d[i] == 0:
                t.remove(i)
            res[ci]+=1
            if not t:
                ci += 1
                res.append(0)
        
        return res[:len(res)-1]