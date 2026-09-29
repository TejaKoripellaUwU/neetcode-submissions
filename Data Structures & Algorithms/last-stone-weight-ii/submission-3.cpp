class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int sum = std::accumulate(stones.begin(),stones.end(),0);
        int targ = sum / 2;
        std::vector<int> cur(targ+1,0);
        std::vector<int> prev(targ+1,0);

        for (int i = 1; i<stones.size()+1; i++){
            for (int j = 0; j<targ+1; j++){
                cur[j] = prev[j];
                if (j-stones[i-1] >= 0 && abs(prev[j-stones[i-1]]+stones[i-1] - targ) < abs(cur[j] - targ)){
                    cur[j] = prev[j-stones[i-1]]+stones[i-1];
                }
            }
            std::swap(cur,prev);
        }
        return 2*abs(targ - prev[targ]) + sum%2;
    }
};