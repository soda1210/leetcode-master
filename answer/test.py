class Test:

    def __init__(self):
        self.a = 1
        self.b = 2

    def add(self):
        return self.a + self.b

    def set(self, x, y):
        self.a, self.b = x, y
        return True


if __name__ == '__main__':
    test = Test()
    ans = test.add()
    print(test.add())
    print(test.set(2, 3))
