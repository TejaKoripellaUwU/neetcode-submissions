class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t0 = False
        t1 = False
        t2 = False
        for i,j,k in triplets:
            if i<= target[0] and j<= target[1] and k<= target[2]:
                if i == target[0]:
                    t0 = True
                if j == target[1]:
                    t1 = True
                if k == target[2]:
                    t2 = True

        return t0 and t1 and t2