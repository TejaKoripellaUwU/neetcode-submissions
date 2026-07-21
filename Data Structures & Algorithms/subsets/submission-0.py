class Solution:
    def dfs(self,a,c):
        if not a:
            # print(c)
            self.res.append(c.copy())
        if len(a)>0:
            print(a,a[1:])
            c.append(a[0])
            self.dfs(a[1:],c)
            c.pop()
            self.dfs(a[1:],c)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums,[])
        # print(res)
        return self.res