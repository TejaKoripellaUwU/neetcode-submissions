class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, std::vector<string>> cache;
        for (string& s:strs){
            string s_copy = s;
            std::sort(s_copy.begin(),s_copy.end());
            cache[s_copy].push_back(s);
        }
        std::vector<std::vector<string>> res;
        for (const std::pair<string,std::vector<string>>& ele : cache){
            res.push_back(ele.second);
        }
        return res;
    }
};
