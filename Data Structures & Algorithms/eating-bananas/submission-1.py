class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p1 = 1
        p2 = max(piles)
        iters = 0
        best_targ = max(piles)
        while p1<=p2:
            iters+=1
            if iters==45:
                break
            total_h = 0
            target = (p2-p1)//2 + p1
            for i in piles:
                total_h += math.ceil(i/target)
            print(target)
            if target == 2:
                print(total_h)
            if total_h>h:
                p1 = target + 1
            elif total_h<=h:
                if target < best_targ: best_targ = target
                p2 = target - 1
        return best_targ