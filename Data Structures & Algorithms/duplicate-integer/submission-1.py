class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            targ_val = nums[i]
            for l in range (len(nums)):
                if targ_val == nums[l] and l != i:
                    return True
        return False