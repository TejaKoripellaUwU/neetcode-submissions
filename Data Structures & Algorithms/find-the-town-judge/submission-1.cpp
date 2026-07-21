class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        std::unordered_map<int,std::vector<int>> outgoing;
        std::unordered_map<int,std::vector<int>> incoming;
        for (auto& vec:trust){
            outgoing[vec[0]].push_back(vec[1]);
            incoming[vec[1]].push_back(vec[0]);
        }
        std::unordered_set<int> c1;
        std::unordered_set<int> c2;
        std::unordered_set<int> res;
        for (int i = 1; i < n+1; ++i){
            if (!outgoing.contains(i)){
                c1.insert(i);
            }
        }
        for (int i = 1; i < n+1; ++i){
            if (incoming[i].size() == n-1){
                c2.insert(i);
            }
        }
        std::set_intersection(c1.begin(),c1.end(),c2.begin(),c2.end(),std::inserter(res,res.begin()));
        if (res.size() == 1){
            return *res.begin();
        }
        return -1;
    }
};