class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for ind in range(len(nums)):
            trip = nums[ind]
            d = dict()
            for j in range(len(nums)):
                if j == ind:
                    continue
                d[nums[j]] = j

            for j in range(len(nums)):
                if j == ind:
                    continue
                if -trip-nums[j] in d and d[-trip-nums[j]] != ind and d[-trip-nums[j]] != j:
                    res.add(tuple(sorted([trip, -trip-nums[j], nums[j]])))
        return [list(i) for i in res]