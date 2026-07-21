class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * len(s)
        for i in range(len(dp)):
            if s[:i+1] in wordDict:
                dp[i] = True
                continue
            for j in range(0,i):
                if dp[j] and s[j+1:i+1] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]