class Solution:
    def word_reachable(self, w1,w2):
        num = 0
        for ind in range(len(w1)):
            if w1[ind] != w2[ind]:
                num+=1
        return num <= 1
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = [(beginWord,1)]
        v = set()

        while q:
            w,l = q.pop(0)
            if w == endWord:
                return l 
            for i in wordList:
                if i not in v and self.word_reachable(w,i):
                    v.add(i)
                    q.append((i,l+1))

        return 0
                 
            
        