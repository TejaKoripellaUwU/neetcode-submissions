class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        postfix = []
        v = 0
        for index,val in enumerate(nums):
            if index == 0:
                prefix.append(1)
                v = val
            else:
                prefix.append(prefix[index-1]*v)
                v = val
        for index in range(len(nums)-1,-1,-1):
            print(index)
            if index == len(nums)-1:
                postfix.append(1)
            postfix.insert(0,postfix[0]*nums[index])
        postfix.pop(0)
        print(prefix)
        print(postfix)
        for pre,post in zip(prefix,postfix):
            res.append(pre*post)

        return res
