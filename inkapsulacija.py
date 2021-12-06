class Point:
    def __init__(self, x = 0, y = 0):
        self.x=x
        self.y=y

pt = Point(1, 2)

print(pt.__dict__)
print(pt.x, pt.y)
print("если перед атрибутом не стоит подчёркиваний, то он открыт и его можно менятьв любом месте кода")
print("если перед атрибутом есть два подчёркивания, то он закрыт и менять его можно только в пределлах класса")

class Red:
    def __init__(self, x = 0, y = 0):
        self.__x=x
        self.__y=y

pt = Red(1, 2)
print(pt.__dict__)
print("print(pt.x, pt.y) не сработает если нет set или get")

class Red2:
    def __init__(self, x = 0, y = 0):
        self.__x=x
        self.__y=y

    def setRed2(self, x, y):
        self.__x = x
        self.__y = y

    def getRed2(self):
        return self.__x, self.__y

pt = Red2(44, 78)
print(pt.getRed2())
pt.setRed2(10, 20)
print(pt.getRed2())










