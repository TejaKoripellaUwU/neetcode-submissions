class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> map;
        int num_l = 0;
        for (char lett : s){
            map[lett]++;
            num_l++;
        }
        for (char lett : t){
            if (map[lett] > 0){
                map[lett]--;
                num_l--;
            } else{
                return false;
            }
        }
        return num_l == 0;
    }
};
