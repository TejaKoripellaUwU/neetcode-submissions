class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if not i.isalpha() and not i.isnumeric():
                s = s.replace(i,"")
        s = s.lower()
        for index in range(0,len(s[0:math.ceil(len(s)-1/2)])):
            if s[index] != s[len(s)-1-index]:
                return False
        return True
