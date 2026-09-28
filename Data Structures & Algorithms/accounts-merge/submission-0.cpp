class Solution {
    struct DSU{
        std::vector<int> rank_arr;
        std::vector<int> mem_arr;

        int find(int e1){
            if (mem_arr[e1] == e1){
                return e1;
            }
            int i = find(mem_arr[e1]);
            mem_arr[e1] = i;
            return i;
        }

        void unio(int e1,int e2){
            int r1 = find(e1);
            int r2 = find(e2);
            if (rank_arr[r1] > rank_arr[r2]){
                mem_arr[r2] = r1;
            } else if (rank_arr[r2] > rank_arr[r1]){
                mem_arr[r1] = r2;
            } else{
                rank_arr[r1]++;
                mem_arr[r2] = r1;
            }
        }

    };
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        // email to DSU index, name
        std::unordered_map<std::string, std::pair<int,std::string>> m;
        // dsu index to email
        std::unordered_map<int, std::string> d;
        DSU dsu {};
        int cur_id = 0;
        for (auto& i: accounts){
            for (int j = 1; j<i.size(); j++){
                if (!m.contains(i[j])){
                    m[i[j]] = std::pair<int, std::string>{cur_id,i[0]};
                    d[cur_id] = i[j];
                    cur_id++;
                    dsu.mem_arr.push_back(m[i[j]].first);
                    dsu.rank_arr.push_back(1);
                }

            }
        }
        for (auto& i: accounts){
            for (int j = 1; j<i.size()-1; j++){
                dsu.unio(m[i[j]].first,m[i[j+1]].first);
            }
        }
        std::vector<std::vector<std::string>> res;
        for (int i = 0; i<cur_id; i++){
            res.push_back(std::vector<std::string>{});
        }
        for (int i=0; i<cur_id; i++){
            int p = dsu.find(dsu.mem_arr[i]);
            res[p].push_back(d[i]);
        }
        std::vector<std::vector<std::string>> fr;

        for (auto& j: res){
            if (j.size() ==0){
                continue;
            }
            std::sort(j.begin(),j.end());
            j.insert(j.begin(),m[j[0]].second);
            fr.push_back(std::move(j));
        }
        return fr;
    }
};