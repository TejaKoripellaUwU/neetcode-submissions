class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(1,len(height)-1):
            l = max(height[:i])
            r = max(height[i+1:])
            total += max(min(l,r)-height[i],0)

        return total