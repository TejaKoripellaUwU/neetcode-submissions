class Solution:
    def numDecodings(self, s: str) -> int:
        # for i in range(len(s)):
        #     s[i] = int(s[i])

        dp = [0] * len(s)
        for i in range(len(s)):
            if i == 0:
                if s[i] == "0":
                    return 0
                else:
                    dp[i] = 1
            
            elif i == 1:
                if int(s[0] + s[i]) <= 26 and s[i] != "0":
                    dp[i] = 2

                elif s[i] == "0":
                    if s[i-1] == "1" or s[i-1] == "2":
                        dp[i] = 1
                    else:
                        return 0
                else:
                    dp[i] = 1
            
            elif s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif s[i-1] == "0" or int(s[i-1]+s[i]) > 26:
                dp[i] = dp[i-1]
            
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
            