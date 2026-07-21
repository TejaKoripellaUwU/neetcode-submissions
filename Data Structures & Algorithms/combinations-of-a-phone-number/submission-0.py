class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(digits)
        res = []

        d = {
        2:["A","B","C"],
        3:["D","E","F"],
        4:["G","H","I"],
        5:["J","K",'L'],
        6:["M","N","O"],
        7:["P","Q","R","S"],
        8:["T","U","V"],
        9:["W","X","Y","Z"]
        } 
        def backtrack(cur,ind):
            if ind >= len(digits):
                res.append(cur)
                return
            for i in d[int(digits[ind])]:
                backtrack(cur+i.lower(),ind+1)
            return
        backtrack("",0)
        if not len(digits):
            return []
        return res