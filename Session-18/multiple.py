class Base1:
    def __init__(self) -> None:
        print("Base1")

    def run(self):
        return "Run for your life!!!"


class Base2:
    def __init__(self) -> None:
        print("Base2")

    def run(self):
        return "Run for my life!"


class MultiBase(Base1, Base2):
    def __init__(self) -> None:
        super().__init__()


if __name__ == "__main__":
    multi = MultiBase()
    print(multi.run())
    print(MultiBase.mro())
