class Solution {
    public int[] twoSum(int[] numbers, int target) {
       int p1 = 0;
       int p2 = numbers.length-1;
       int[] sol = new int[2];
       boolean c = false;
       while (!c){
        System.out.println("p1:"+p1);
        System.out.println("p2:"+p2);
            if (numbers[p1] + numbers[p2] == target){
                sol[0] = p1+1;
                sol[1] = p2+1;
                c = true;
                return sol;
            }
            if (numbers[p1] + numbers[p2] < target){
                p1++;
            }
            else if (numbers[p1] + numbers[p2] > target){
                p2--;
            }
       }
       return sol;
    }
}
