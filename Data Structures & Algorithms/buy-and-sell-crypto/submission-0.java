class Solution {
    public int maxProfit(int[] prices) {
        int p1 = 0;
        int p2 = 1;
        int bestP = 0;
        while (p2 < prices.length){
            int res = prices[p2]-prices[p1];
            if (res > bestP){
                bestP = res;
            } else if (res<0){
                p1 = p2;
            }
            p2++;
        }
        return bestP;
    }
}
