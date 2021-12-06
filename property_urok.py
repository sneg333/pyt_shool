# объекты - свойства property -- наследование
class Person():
    def can_work(self):
        print('я могу ходить')

    def can_brith(self):
        print('я могу дышать')

class Doctor(Person):
    def lecht(self):
        print('я могу лечить')

class Ortoped(Doctor):
    pass

class Arhitektir(Person):
    def a_work(self):
        print('я могу строить')

d = Doctor()
d.lecht()
d.can_work()
d.can_brith()

a = Arhitektir()
a.a_work()
a.can_work()
a.can_brith()

print(issubclass(Doctor, Person))
print(isinstance(d, Doctor))
print(isinstance(d, Person))
e = Ortoped()
e.can_brith()

