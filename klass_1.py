class Ferst:
    'комментарий к классу'
    x = 1
    y = 10

#вызываем переменную класса
print(Ferst.x)
print(Ferst.__doc__)
print(Ferst.__name__)

pt = Ferst()


Ferst.x = 100
print(pt.x, pt.y)
