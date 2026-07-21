class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque([[heights[0],0]])
        m = 0
        for i in range(len(heights)):
            if heights[i]>= stack[0][0]:
                stack.appendleft([heights[i],i])
            else:
                for ele in range(len(stack)):
                    if heights[i]<stack[ele][0]:
                        m = max(stack[ele][0]*(i-stack[ele][1]),m)
                        stack[ele] = (heights[i],stack[ele][1])
                    else:
                        break

        for ele in range(len(stack)):
            m = max(stack[ele][0]*(len(heights)-stack[ele][1]),m)
        return m