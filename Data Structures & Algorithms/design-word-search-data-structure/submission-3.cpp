struct TrieNode{
    char let;
    bool endWord = false;
    unordered_map<char,TrieNode*> next;
};

class WordDictionary {
public:
    TrieNode* root;
    WordDictionary() {
        root = new TrieNode{};
    }
    
    void addWord(string word) {
        TrieNode* cur = root;
        for (auto let:word){
            if (!cur->next.contains(let)){
                TrieNode* n = new TrieNode{.let = let};
                cur->next[let] = n;
            }
            cur = cur->next[let];
        }
        cur->endWord = true;
    }
    bool recurse(string& word, int curChar, TrieNode* curNode){
        if (curChar == word.length()){
            return curNode->endWord;
        }
        if (word[curChar] == '.'){
            for (auto iter = curNode->next.begin(); iter!=curNode->next.end(); ++iter){
                if (recurse(word,curChar+1,iter->second)){
                    return true;
                }
            }
            return false;
        } else{
            if (curNode->next.contains(word[curChar])){
                return recurse(word,curChar+1,curNode->next[word[curChar]]);
            } else{
                return false;
            }
        }
    }
    bool search(string word) {
        return recurse(word,0,root);
    }
};
