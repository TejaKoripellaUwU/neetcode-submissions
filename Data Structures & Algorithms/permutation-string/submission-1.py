class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p1 = 0
        p2 = len(s1)-1
        sd = {}
        orig = {}
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            sd.update({s2[i]:sd.get(s2[i],0)+1})
            orig.update({s1[i]:orig.get(s1[i],0)+1})

        if orig == sd:
            return True
        while p2 < len(s2)-1:
            print(sd)
            if sd[s2[p1]] == 1:
                del sd[s2[p1]]
            else:
                sd[s2[p1]] -= 1
            p1 +=1
            p2 += 1       
            sd.update({s2[p2]:sd.get(s2[p2],0)+1})
            if orig == sd:
                return True
        return False   
            