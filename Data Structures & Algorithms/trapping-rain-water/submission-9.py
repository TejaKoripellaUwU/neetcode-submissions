class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        maxRight = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                maxLeft[i] = 0
            else:
                maxLeft[i] = max(maxLeft[i-1],height[i-1])
        
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                maxRight[i] = 0
            else:
                maxRight[i] = max(maxRight[i+1],height[i+1])
        
        res = 0
        for i in range(len(height)):
            res+=max(min(maxLeft[i],maxRight[i])-height[i],0)
        print(maxLeft)
        print(maxRight)

        return res