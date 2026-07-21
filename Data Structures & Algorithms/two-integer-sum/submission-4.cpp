class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> cache;
        for (int i = 0; i<nums.size(); i++){
            cache[target-nums[i]] = i;
        }
        for (int i = 0; i<nums.size(); i++){
            if (cache.contains(nums[i]) && i != cache[nums[i]]){
                vector<int>v{i,cache[nums[i]]};
                sort(v.begin(),v.end());
                return v;
            }
        }
        return vector<int>{};
    }
};
