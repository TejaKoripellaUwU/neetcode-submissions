class Solution {
    struct fpair{
        int freq;
        char c;
    };

    struct fpairComp{
        bool operator()(const fpair& a, const fpair& b){
            return a.freq < b.freq;
        }
    };
public:
    string longestDiverseString(int a, int b, int c) {

        std::priority_queue<fpair,vector<fpair>,fpairComp> pq(fpairComp{});
        if (a > 0){pq.push(fpair{a,'a'});}
        if (b > 0){pq.push(fpair{b,'b'});}
        if (c > 0){pq.push(fpair{c,'c'});}

        std::string res = "";
        while (pq.size()>0){
            auto [freq,c] = pq.top();
            pq.pop();
            int l = res.size();
            if (l >= 2 && res[l-2] == res[l-1] && res[l-1] == c){
                if (pq.size() > 0){
                    auto [freq2,c2] = pq.top();
                    pq.pop();
                    res += c2;
                    if (freq2 > 1){
                        pq.push(fpair{freq2-1,c2});
                    }
                } else {
                    return res;
                }
            } else{
                res += c;
                freq -= 1;
            }
            if (freq > 0){pq.push(fpair{freq, c});}
        }
        return res;
        
    }
};