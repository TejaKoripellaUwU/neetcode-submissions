class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = dict()
        wordDict = set(wordDict)
        def dfs(i):
            if i in memo:
                # print(i, "memo")
                return memo[i]
            if i >= len(s):
                return True
            sub = ""
            for j in range(i, len(s)):
                sub += s[j]
                # print(sub)
                if sub in wordDict:
                    res = dfs(j+1)
                    # print(res,sub)
                    memo[i] = res
                    if res:
                        return True
            # print("failed")
            memo[i] = False
            return False

        return dfs(0)
