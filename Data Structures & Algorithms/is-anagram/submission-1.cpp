class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char,int> w1;
        std::unordered_map<char,int> w2;
        for (auto w : s){
            w1[w]++;
        }
        for (auto w : t){
            w2[w]++;
        }
        return w1 == w2;
    }
};
