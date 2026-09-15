class MedianFinder {
public:
    //min heap
    std::priority_queue<int,std::vector<int>, std::greater<int>> high;
    //max heap
    std::priority_queue<int,std::vector<int>, std::less<int>> low;

    MedianFinder() {

    }

    void addNum(int num) {
        if (high.empty() || num >= high.top()){
            high.push(num);
        } else{
            low.push(num);
        }
        if (high.size() > low.size()+1){
            low.push(high.top());
            high.pop();
        } else if (low.size() > high.size()+1){
            high.push(low.top());
            low.pop();
        }
    }
    
    double findMedian() {
        if (high.size() == low.size()){
            return (double) (high.top() + low.top())/2.0;
        }
        if (high.size() > low.size()){
            return (double) high.top();
        } else{
            return (double) low.top();
        }
        
    }
};
