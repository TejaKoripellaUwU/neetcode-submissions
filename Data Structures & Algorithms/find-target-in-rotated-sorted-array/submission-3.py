class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = (r+l)//2
        c = 6
        while (nums[l]>nums[r] and c>0):
            m = (r+l)//2
            c-=1
            print(l,r,m)

            if target == nums[m]:
                return m
            if target == nums[r]:
                return r
            if target == nums[l]:
                return l

            if target > nums[l]:
                if target > nums[m]:
                    l = m+1
                    m = l
                elif target < nums[m]:
                    r = m-1
                    m = r
            elif target < nums[l]:
                if target > nums[m]:

                    print('f')
                    r = m-1
                    m = r
                elif target < nums[m]:
                    print('t')
                    l = m+1
                    m = l

            else:
                return m

        sub_arr = []
        less = True
        if target>nums[m]:
            less = False
            sub_arr = nums[m:]
        elif target<nums[m]:
            sub_arr = nums[:m+1]
        else:
            return m
        print(m,sub_arr)
        l = 0
        r = len(sub_arr)-1
        while(l<=r):
            t = (r+l)//2
            if target < sub_arr[t]:
                r = t-1
            elif target > sub_arr[t]:
                l = t+1
            else:
                if not less:
                    return m+t
                return t

        return -1

            