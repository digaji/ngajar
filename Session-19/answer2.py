from math import pi


class Circle:
    def __init__(self, radius: float = 1.0, color: str = "red") -> None:
        self.__radius = float(radius)
        self.__color = color

    def getRadius(self) -> float:
        return self.__radius

    def setRadius(self, radius: float) -> None:
        self.__radius = float(radius)

    def getColor(self) -> str:
        return self.__color

    def setColor(self, color: str) -> None:
        self.__color = color

    def toString(self) -> str:
        return f"Radius: {self.__radius}\nColor: {self.__color}"

    def getArea(self) -> float:
        return pi * (self.__radius ** 2)


class Cylinder(Circle):
    def __init__(self, radius: float = 1.0, color: str = "red", height: float = 1.0) -> None:
        super().__init__(radius, color)
        self.__height = float(height)

    def getHeight(self) -> float:
        return self.__height

    def setHeight(self, height: float) -> None:
        self.__height = float(height)

    def toString(self) -> str:
        return f"Radius: {self.__radius}\nColor: {self.__color}\nHeight: {self.__height}"

    def getVolume(self) -> float:
        return self.getArea() * self.__height


if __name__ == "__main__":
    myCyli = Cylinder(5, "black", 10)
    print("Original data")
    print(f"Radius: {myCyli.getRadius()}")
    print(f"Color: {myCyli.getColor()}")
    print(f"Height: {myCyli.getHeight()}")
    print(f"Volume: {myCyli.getVolume()}")

    print("\nModified data")
    myCyli.setRadius(10)
    myCyli.setColor("blue")
    myCyli.setHeight(100)
    print(f"Radius: {myCyli.getRadius()}")
    print(f"Color: {myCyli.getColor()}")
    print(f"Height: {myCyli.getHeight()}")
    print(f"Volume: {myCyli.getVolume()}")
