class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        string res;
        res.reserve(a + b + c);
        int cnt[3] = {a, b, c};

        for (int i = 0, total = a + b + c; i < total; ++i) {
            int best = -1;
            for (int j = 0; j < 3; ++j) {
                if (cnt[j] == 0) continue;
                size_t n = res.size();
                if (n >= 2 && res[n-1] == 'a' + j && res[n-2] == 'a' + j) continue;
                if (best == -1 || cnt[j] > cnt[best]) best = j;
            }
            if (best == -1) break;
            res += char('a' + best);
            cnt[best]--;
        }
        return res;
    }
};