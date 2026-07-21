class TrieNode:
    def __init__(self,val,end):
        self.children = dict()
        self.val = val
        self.end = end
    
    def add_child(self,child:TrieNode):
        self.children[child.val] = child

class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None,False)

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i in cur.children:
                cur = cur.children[i]
            else:
                cur.add_child(TrieNode(i,False))
                cur = cur.children[i]
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i in cur.children:
                cur = cur.children[i]

            else:
                return False

        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return False
        
        return True
        