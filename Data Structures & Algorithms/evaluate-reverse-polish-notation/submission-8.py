
class Solution:
    def evalfunc(self,n1,n2,op):
        if op == "+":
            return n1+n2
        if op == "-":
            return n2-n1
        if op == "*":
            return n1*n2
        if op == "/":
            return int(n2/n1) 

    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+","-","*","/"}
        m = []
        os = deque()
        ns = deque()
        for i in tokens:
            print(ns)
            if i not in ops:
              ns.append(int(i))
            elif i in ops:
                ns.append(self.evalfunc(int(ns.pop()),int(ns.pop()),i))
        return ns.pop()
            # if i in ops:
            #     os.append(i)
            #     m = []
            # else:
            #     ns.append(i)
            #     m.append(i)
            #     if len(m) == 2:
            #         res = int(self.evalfunc(int(ns.pop()),int(ns.pop()),os.pop()))
            #         while len(ns)>0:
            #             res = int(self.evalfunc(int(res),int(ns.pop()),os.pop()))
            #         ns.append(int(res))
            #         m = [res]
        # print(type(ns[-1]))
        return ns.pop()

