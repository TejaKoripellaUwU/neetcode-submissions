class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] is the max longest subsequence terminating at i, the soln is max of dp
        dp = [1]* len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)