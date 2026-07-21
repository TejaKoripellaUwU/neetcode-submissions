class Solution {
public:

    string encode(vector<string>& strs) {
        string out;
        for (auto& str : strs) {
            out += std::to_string(str.size()) + "#" + str;
        }
        return out;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while (i < s.size()) {
            int j = s.find('#', i);
            int len = std::stoi(s.substr(i, j - i));
            res.push_back(s.substr(j + 1, len));
            i = j + 1 + len;
        }
        return res;
    }
};