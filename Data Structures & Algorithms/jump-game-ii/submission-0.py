class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [1000000000]*len(nums)
        dp[-1] = 0
        for i in range(len(dp)-1,-1,-1):
            for j in range(i+1,min(i+nums[i]+1,len(dp))):
                dp[i] = min(1+dp[j],dp[i])
        return dp[0]