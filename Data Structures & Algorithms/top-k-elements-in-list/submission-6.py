class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm = {}
        for val in nums:
            hashm.update({val:hashm.get(val,0)+1})
        print(hashm)
        hashm2 = {}
        for key in hashm.keys():
            item = hashm2.get(hashm[key],[])
            item.append(key)
            hashm2.update({hashm[key]:item})
        print(hashm2)
        res = []
        n = 0
        print(list(hashm2.keys())[:k+1])
        for i in sorted(list(hashm2.keys()),reverse = True):
            for m in hashm2[i]:
                if len(res)>=k:
                    return res
                res.append(m)
        return res
        
