class MinStack:
    def __init__(self):
        self.minS = []
        self.s2 = []

    def push(self, val: int) -> None:
        self.s2.append(val)
        if not self.minS or val <= self.minS[-1]:
            self.minS.append(val)

    def pop(self) -> None:
        if not self.s2:
            return None
        else:
            val = self.s2.pop()
        if val == self.minS[-1]:
            self.minS.pop()

    def top(self) -> int:
        if not self.s2:
            return None
        else:
            return self.s2[-1]

    def getMin(self) -> int:
        if not self.minS:
            return None
        return self.minS[-1]
