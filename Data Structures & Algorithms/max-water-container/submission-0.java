class Solution {
    public int maxArea(int[] heights) {
        int maxArea = 0;
        int p1 = 0;
        int p2 = heights.length - 1;
        while (p1 <= heights.length-1 && p2 >= 0){
            int curArea = Math.abs((p1-p2))*(Math.min(heights[p2],heights[p1]));
            maxArea = (curArea>maxArea) ? curArea : maxArea;
            if (heights[p1]>heights[p2]){
                p2--;
            }else{
                p1++;
            }
            // else:p1 ++
            
        }
        return maxArea;
    }
}
