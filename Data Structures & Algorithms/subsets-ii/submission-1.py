class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def backtrack(i,cur):
            if i >= len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i+1,cur)
            cur.pop(-1)

            i += 1
            while i<len(nums) and nums[i] == nums[i-1]:
                i+=1
            backtrack(i,cur)
            return
        
        backtrack(0,[])
        return res