class Solution:
    def rob(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            r1 = -1
            r2 = -1
            if index>=2:
                r1 = nums[index-2]+nums[index]
                r2 = nums[index-1]
            elif index>=1:
                r1 = nums[index]
                r2 = nums[index-1]
            elif index == 0:
                continue
            print(r1,r2)
            nums[index] = max(r1,r2)
        print(nums)
        return nums[-1]


                