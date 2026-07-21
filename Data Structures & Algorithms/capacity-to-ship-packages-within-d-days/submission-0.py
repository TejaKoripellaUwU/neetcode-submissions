class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def evaly(cap):
            res = 1
            cur_cap = 0
            for i in weights:
                if i>cap:
                    return False
                cur_cap += i
                if cur_cap > cap:
                    res+=1
                    cur_cap = i

            return res <= days
        
        mi = max(weights)
        ma = sum(weights)
        last = ma
        while mi<=ma:
            mid = (mi+ma)//2
            re = evaly(mid)
            print(mi,ma,mid,re)

            if re:
                last = mid
                ma = mid-1
            else:
                mi = mid+1

        return last



