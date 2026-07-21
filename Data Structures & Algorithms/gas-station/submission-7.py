class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot = 0
        cur = 0
        targ_ind = 0
        f = True
        if (sum(gas) - sum(cost)) < 0:
            return -1

        t = 0
        while (cur != targ_ind or f) and t < (len(gas)-1)*2:
            if tot < 0:
                targ_ind = cur
                tot = 0
            
            tot+=gas[cur]-cost[cur]
            print(tot, cur, targ_ind)
            cur+=1
            t += 1
            cur = cur%len(gas)
        return targ_ind