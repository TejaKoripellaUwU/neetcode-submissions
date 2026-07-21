class Solution:
    def isValid(self, s: str) -> bool:
        mdict = {'}':'{',']':'[',')':'('}
        q = deque()
        for i in s:
            if len(q)>0 and i in mdict:
                v = q.pop()
                if mdict[i] != v:
                    return False
            else:
                q.append(i)
        print(len(q))
        return len(q) == 0
                     
        