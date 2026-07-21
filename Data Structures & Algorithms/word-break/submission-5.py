class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        class trieNode:
            def __init__(self,val = None,endWord = False):
                self.nodes = dict()
                self.val = val
                self.endWord = endWord

        class trie:
            def __init__(self):
                self.root = trieNode()
            
            def addWord(self,word):
                curNode = self.root
                for ind,i in enumerate(word):
                    if i in curNode.nodes.keys():
                        curNode = curNode.nodes[i]
                        if ind == len(word)-1:
                            curNode.endWord = True
                    else:
                        newNode = trieNode(val = i, endWord = (ind == len(word)-1))
                        curNode.nodes[i] = newNode
                        curNode = curNode.nodes[i]

            def search(self, word):
                curNode = self.root
                for ind,i in enumerate(word):
                    if i in curNode.nodes.keys():
                        if (ind == len(word)-1):
                            return True
                        curNode = curNode.nodes[i]
                    else:
                        return False
        t = trie()
        for i in wordDict:
            t.addWord(i)
        
        dp = [False] * (len(s)+1)
        dp[-1] = True
        maxlen = len(max(wordDict))
        print(t.root.nodes.keys())
        for i in range(len(s)-1,-1,-1):
            tn = t.root
            for j in range(i,len(s)):
                print(i,j,s[j],i+maxlen,len(s))
                if s[j] in tn.nodes.keys():
                    print(s[i:j+1]," in keys")
                    tn = tn.nodes[s[j]]
                    print(tn.val,tn.endWord)
                    if tn.endWord:
                        print(s[i:j+1], " is a word")
                        dp[i] = dp[j+1]
                        if dp[i]: break
                else:
                    print(s[i:j+1], " not a wrod")
                    break
        print(dp)
        return dp[0]



        
            
            

