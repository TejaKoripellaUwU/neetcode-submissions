
class MinStack:

    def __init__(self):
        self.q = deque()
        self.v = deque()
        self.v.append(math.inf)
    def push(self, val: int) -> None:
        if val<=self.v[-1]:
            self.v.append(val)
        self.q.append(val)

    def pop(self) -> None:
        if self.q[-1] == self.v[-1]:
            self.v.pop()
        self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.v[-1]
