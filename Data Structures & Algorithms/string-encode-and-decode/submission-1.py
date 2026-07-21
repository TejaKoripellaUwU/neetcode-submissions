class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))+"#"+i
        res+="3#"
        return res

    def decode(self, s: str) -> List[str]:
        skip_char = "" 
        res = []
        curstring = ""
        firstpass = True
        for index,char in enumerate(s):
            if skip_char == 0:
                skip_char = char

            elif char == "#" and type(skip_char) == str:
                print(skip_char)
                skip_char = int(skip_char)
                if firstpass:
                    firstpass = False
                    pass
                else:
                    res.append(curstring)
                    curstring = ""

            elif type(skip_char) == str:
                skip_char += char

            elif type(skip_char) == int and skip_char>0:
                curstring+=char
                skip_char-=1
        return res

