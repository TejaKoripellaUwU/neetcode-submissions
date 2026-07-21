class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        def helper(left, right):
            if left > right:
                return ""
            if right - left + 1 <= 1:
                return s[left:right+1]

            best = ""
            for center in range(left, right + 1):
                p1 = expandAroundCenter(center, center)
                if len(p1) > len(best):
                    best = p1
                p2 = expandAroundCenter(center, center + 1)
                if len(p2) > len(best):
                    best = p2

            mid = (left + right) // 2
            leftBest = helper(left, mid - 1)
            rightBest = helper(mid + 1, right)

            return max([best, leftBest, rightBest], key=len)

        return helper(0, len(s) - 1)
