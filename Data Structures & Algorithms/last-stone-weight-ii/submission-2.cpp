class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int sum = std::accumulate(stones.begin(),stones.end(),0);
        int targ = sum / 2;
        std::vector<std::vector<int>> dp(stones.size()+1, std::vector<int>(targ+1,0));
        for (int i = 1; i<stones.size()+1; i++){
            for (int j = 0; j<targ+1; j++){
                dp[i][j] = dp[i-1][j];
                if (j-stones[i-1] >= 0 && abs(dp[i-1][j-stones[i-1]]+stones[i-1] - targ) < abs(dp[i][j] - targ)){
                    dp[i][j] = dp[i-1][j-stones[i-1]]+stones[i-1];
                }
            }
        }
        return 2*abs(targ - dp[stones.size()][targ]) + sum%2;
    }
};