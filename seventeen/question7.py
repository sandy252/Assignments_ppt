class FrontMiddleBack:
    def __init__(self):
        self.front = []
        self.back = []

    def pushFront(self, val: int) -> None:
        self.front.append(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        mid = len(self.front) // 2
        self.front.insert(mid, val)
        self.balance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self.balance()

    def popFront(self) -> int:
        if self.front:
            return self.front.pop()
        elif self.back:
            self.front = self.back[::-1]
            self.back = []
            return self.front.pop()
        else:
            return -1

    def popMiddle(self) -> int:
        if self.front:
            mid = (len(self.front) - 1) // 2
            return self.front.pop(mid)
        elif self.back:
            self.front = self.back[::-1]
            self.back = []
            mid = (len(self.front) - 1) // 2
            return self.front.pop(mid)
        else:
            return -1

    def popBack(self) -> int:
        if self.back:
            return self.back.pop()
        elif self.front:
            return self.front.pop(0)
        else:
            return -1

    def balance(self) -> None:
        if len(self.front) > len(self.back) + 1:
            self.back.append(self.front.pop())
        elif len(self.front) < len(self.back):
            self.front.append(self.back.pop())
