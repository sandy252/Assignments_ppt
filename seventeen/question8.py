class DataStream:
    def __init__(self, value, k):
        self.stream = []
        self.value = value
        self.k = k

    def consec(self, num):
        self.stream.append(num)

        if len(self.stream) > self.k:
            self.stream.pop(0)

        return self.stream == [self.value] * self.k
