class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> m;
        for (int i = 0; i<nums.size();i++){
            if (m.contains(nums[i])){
                return true;
            }
            m.insert(nums[i]);
        }
        return false;
    }
};