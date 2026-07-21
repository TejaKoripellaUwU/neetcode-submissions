class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> l;
        int total = 1;
        for (auto& n: nums){
            l.push_back(total);
            total = total * n;
        }
        int total2 = 1;
        for (int i = nums.size()-1; i>=0; i--){
            l[i] = l[i]*total2;
            total2 = total2 * nums[i];
        }
        return l;
    }
};
