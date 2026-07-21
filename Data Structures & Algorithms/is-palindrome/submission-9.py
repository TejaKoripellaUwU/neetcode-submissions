class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s)-1
        while p1<p2:
            while not (s[p1].isalpha() or s[p1].isnumeric()) and p1<p2 :
                p1 +=1

            while not (s[p2].isalpha() or s[p1].isnumeric()) and p1<p2:
                p2 -= 1
            
            print(s[p1].lower(), s[p2].lower())
            if s[p1].lower() != s[p2].lower():
                return False
            else:
                p1+=1
                p2-=1
        return True