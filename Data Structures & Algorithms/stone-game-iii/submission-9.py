class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        import sys
        sys.setrecursionlimit(100000)

        min_dict = dict()
        max_dict = dict()

        def maxi(ind,takes):
            if (ind,takes) in max_dict:
                return max_dict[(ind,takes)]

            if ind >= len(stoneValue):
                return 0

            if takes == 3:
                if (ind,0) not in min_dict:
                    min_dict[(ind,0)] = mini(ind,0)
                max_dict[(ind,takes)] = min_dict[(ind,0)]
                return max_dict[(ind,takes)]

            if takes == 0:
                max_dict[(ind,takes)] = maxi(ind+1,takes+1)+stoneValue[ind]
                return max_dict[(ind,takes)]

            max_dict[(ind,takes)] = max(
                maxi(ind+1,takes+1)+stoneValue[ind],
                mini(ind,0)
            )
            return max_dict[(ind,takes)]

        def mini(ind,takes):
            if (ind,takes) in min_dict:
                return min_dict[(ind,takes)]

            if ind >= len(stoneValue):
                return 0

            if takes == 3:
                if (ind,0) not in max_dict:
                    max_dict[(ind,0)] = maxi(ind,0)
                min_dict[(ind,takes)] = max_dict[(ind,0)]
                return min_dict[(ind,takes)]

            if takes == 0:
                min_dict[(ind,takes)] = mini(ind+1,takes+1)-stoneValue[ind]
                return min_dict[(ind,takes)]

            min_dict[(ind,takes)] = min(
                mini(ind+1,takes+1)-stoneValue[ind],
                maxi(ind,0)
            )
            return min_dict[(ind,takes)]

        res = maxi(0,0)

        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        return "Tie"