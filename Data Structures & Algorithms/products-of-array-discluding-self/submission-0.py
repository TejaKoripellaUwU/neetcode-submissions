class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = 1
        zero_present = 0
        res = []
        for index,value in enumerate(nums):
            if value != 0:
                full_product = full_product * value
            else:
                zero_present += 1
        for i in nums:
            if zero_present == 1:
                if i == 0:
                    res.append(full_product)
                else:
                    res.append(0)
            elif zero_present > 1:
                res.append(0)

            elif zero_present == 0:
                res.append(full_product//i)

        return res