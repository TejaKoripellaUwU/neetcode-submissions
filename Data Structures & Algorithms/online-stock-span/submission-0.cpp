class StockSpanner {
public:
    std::vector<std::pair<int,int>> vals{};
    int cur_day = 0;
    StockSpanner() {
    }
    
    int next(int price) {
        cur_day += 1;
        while (vals.size() && price >= vals[vals.size()-1].first){
            vals.pop_back();
        }

        int res = vals.size() ? cur_day - vals[vals.size()-1].second : cur_day;
        vals.push_back(std::pair<int,int>{price,cur_day});
        return res;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */