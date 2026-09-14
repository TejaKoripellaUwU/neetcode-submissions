class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums)
        if nums[0] > nums[-1]:
            while p1 < p2:
                m = (p1+p2)//2
                if nums[m] >= nums[0]:
                    p1 = m + 1
                else:
                    p2 = m
        print(p1)
        l = 0
        r = 0
        max_ind = 0
        if nums[p1]<=target<=nums[-1]:
            l = p1
            r = len(nums)
        else:
            l = 0
            r = p1

        max_ind = r
        print(l,r,max_ind)
        while l < r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        if l == max_ind or nums[l] != target:
            return -1
        else:
            return l