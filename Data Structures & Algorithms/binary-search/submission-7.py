class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums)-1
        while lp < rp:
            mid = ((rp-lp)//2) + lp
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                lp = mid + 1
            else:
                rp = mid - 1
        
        if nums[rp] == target:
            return rp
        else:
            return -1
                
        

        
    
