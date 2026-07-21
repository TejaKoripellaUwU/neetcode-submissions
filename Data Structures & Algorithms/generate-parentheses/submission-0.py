class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = dict()
        def dfs(op, st, remaining):
            if remaining == 0 and op == 0:
                return [st]
            
            # if remaining in memo and op == 0:
            #     return memo[remaining]

            res = []
            if op > 0:
                res.extend(dfs(op-1,st+")",remaining))
            if remaining > 0:
                res.extend(dfs(op+1,st+"(",remaining-1))

            
            # if len(stack) == 0:
            #     memo[remaining] = set()
            return res
        return dfs(0,"",n)

        '''
        0 3
        1 2
        0 2
        1 2

        '''