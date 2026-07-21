
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int p2 = 0;
        char[] c = s.toCharArray();
        int t = 1;
        ArrayList<Character> f = new ArrayList<Character>();
        if (c.length == 0){
            return 0;
        }
        f.add(c[p2]);
        p2++;
        while (p2<c.length){
            int r = f.indexOf((Character) c[p2]);
            if (r!=-1){
                if (f.size()>t){
                    t = f.size();
                }
                if (r<f.size()-1){
                    f = new ArrayList<Character>(f.subList(r+1,f.size()));
                } else{
                    f = new ArrayList<Character>();
                }
            } 
            f.add(c[p2]);
            p2++;
        }
        int k = f.size();
        if (k>t){
            return k;
        }
        return t;
    }
}
