class Solution:
    def rob(self, nums: List[int]) -> int:
        arr1 = [0]*(len(nums)-1)
        arr2 = [0]*(len(nums)-1)
        if len(nums)<=1:
            return nums[0]
        for i in range(len(nums)-1):
            if i == 0:
                arr1[i] = nums[i]
            elif i == 1:
                arr1[i] = max(nums[i], nums[i-1])
            else:
                arr1[i] = max(nums[i]+arr1[i-2], arr1[i-1])
        
        for i in range(1,len(nums)):
            if i == 1:
                arr2[i-1] = nums[i]
            elif i == 2:
                arr2[i-1] = max(nums[i], nums[i-1])
            else:
                arr2[i-1] = max(nums[i]+arr2[i-3], arr2[i-2])
        print(arr1,arr2)
        return max(arr1[-1],arr2[-1])