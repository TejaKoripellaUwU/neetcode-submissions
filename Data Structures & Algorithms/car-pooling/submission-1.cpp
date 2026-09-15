class Solution {
    struct tripEvent{
        bool enter;
        int ppl;
        int time;
    };
    struct tripComp{
        bool operator()(const tripEvent& a, const tripEvent& b){
            if (a.time == b.time){
                return a.enter;
            }
            return a.time > b.time;
        }
    };
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        std::priority_queue<tripEvent,std::vector<tripEvent>,tripComp> pq;
        for (auto& e: trips){
            pq.push(tripEvent{.enter = true, .ppl = e[0], .time = e[1]});
            pq.push(tripEvent{.enter = false, .ppl = e[0], .time = e[2]});
        }
        int curppl = 0;
        while (!pq.empty()){
            auto event = pq.top();
            pq.pop();
            if (event.enter){
                curppl += event.ppl;
            } else{
                curppl -= event.ppl;
            }
            if (curppl > capacity){return false;}
        }
        return true;
    }
};