class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1 = 0
        p2 = 1
        curlen = 1
        maxLen = 1
        charDict = {s[p1]:1}
        r = False
        while p2 < len(s):
            if not r:
                charDict.update({s[p2]:charDict.get(s[p2],0)+1})
            total = 0
            m = 0
            for i in charDict.keys():
                total+=charDict[i]
                m = max(m,charDict[i])
            if total-m <= k:
                print(p2)
                p2+=1
                curlen += 1
                maxLen = max(curlen,maxLen)
                r = False
            else:
                charDict[s[p1]] -= 1
                p1+=1
                curlen-=1
                r = True
                
        return maxLen