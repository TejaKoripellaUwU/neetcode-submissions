class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = nums[0]
        mx = nums[0]
        res = mn
        for i in nums[1:]:
            print(mx,mn,"start")
            if i == 0:
                mx = 0
                mn = 0
            else:
                pmax = mx
                mx = max(i*mx,i*mn,i)
                mn = min(i*pmax,i*mn,i)
            print(mx,mn,"end")

            res = max(mx,mn,res)
        return res
