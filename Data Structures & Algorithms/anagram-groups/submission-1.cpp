class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string,vector<string>> m;
        for (auto s: strs){
            string t = s;
            std::sort(t.begin(),t.end());
            m[t].push_back(s);
        }
        std::vector<std::vector<string>> res;
        for (const auto p:m){
            res.push_back(p.second);
        }
        return res;
    }
};
