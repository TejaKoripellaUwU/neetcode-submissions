class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(w1,w2):
            if w1 == "" and w2 == "":
                return 0
            

            if w1 and w2 and w1[0] == w2[0]:
                return dfs(w1[1:],w2[1:])
            
            if not w1:
                return dfs(w1,w2[1:])+1
            
            if not w2:
                return dfs(w1[1:],w2)+1
            
            res = dfs(w1[1:],w2)+1
            res = min(res, dfs(w1,w2[1:])+1)
            res = min(res, dfs(w1[1:],w2[1:])+1)
            return res
        
        return dfs(word1,word2)