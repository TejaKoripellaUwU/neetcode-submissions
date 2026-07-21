class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            d={}
            for m in i:
                d.update({m:d.get(m,0)+1})
            res[hash(frozenset(d.items()))].append(i)

        return res.values()
        