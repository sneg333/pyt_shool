print(" класс может сожержать данные (атрибуты) и методы (функции)")

class Point:
    x = 1
    y = 2
    def setCord(self, x, y):
        self.f=x
        self.t=y

pt = Point()

pt.setCord(4, 3)
print(pt.__dict__)
print("или так")
Point.setCord(pt, 9, 8)
print(pt.__dict__)

class Radar:
    def __init__(self, r = 0,  w = 0 ):
        self.r = r
        self.w = w
    def __del__(self):
        print("удаление экземпляра" + self.__str__())

print("второрой класс старт, __init__ автоматически запускает выполнение")
pt = Radar()
pt2 = Radar(5)
pt3 = Radar(49, 44)
print(pt.__dict__)
print(pt2.__dict__)
print(pt3.__dict__)


