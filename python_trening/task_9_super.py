class A:
    def __init__(self) -> None:
        self.x = 10


class B(A):
    def __init__(self) -> None:
        super().__init__()
        self.y = self.x + 5


obj = B()
print(obj.y)