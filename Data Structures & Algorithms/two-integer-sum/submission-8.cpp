class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
            std::unordered_map<int,int>cache;
            for (int i = 0; i<nums.size();i++){
                cache[nums[i]] = i; 
            }
            for (int i =0; i<nums.size();i++){
                if (cache.contains(target-nums[i]) && i!=cache.at(target-nums[i])){
                    std::vector<int> res = {i, cache[target-nums[i]]};
                    return res;
                }
            }

    }
};
