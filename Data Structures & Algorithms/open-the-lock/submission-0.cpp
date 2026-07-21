class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead(deadends.begin(), deadends.end());
        unordered_set<string> visited;

        if (dead.count("0000")) return -1;

        queue<pair<string, int>> q;
        q.push({"0000", 0});
        visited.insert("0000");

        while (!q.empty()) {
            auto [state, moves] = q.front();
            q.pop();

            if (state == target) return moves;

            for (int i = 0; i < 4; i++) {
                string up = state;
                string down = state;

                up[i] = (up[i] == '9') ? '0' : up[i] + 1;
                down[i] = (down[i] == '0') ? '9' : down[i] - 1;

                if (!dead.count(up) && !visited.count(up)) {
                    visited.insert(up);
                    q.push({up, moves + 1});
                }

                if (!dead.count(down) && !visited.count(down)) {
                    visited.insert(down);
                    q.push({down, moves + 1});
                }
            }
        }

        return -1;
    }
};