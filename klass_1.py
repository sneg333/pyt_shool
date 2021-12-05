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

pt.x = 5
pt.y = 99
print(pt.x, 'и', pt.y, 'таже перменная из первого класса', Ferst.y)

print('getattr(obj, name[, default]) - возвращает значение атрибута объекта')
print(getattr(pt, "x"))
print('hasattr(obj, name) - проверяет на значение атрибута name в obj')
print(hasattr(pt, "y"))
print('setattr(obj, name, value) - задаёт значение атрибута (если атрибут не существует, то он создаёт)')
setattr(pt, "z", 7)
print(pt.__dict__)

print('delattr(ibj, name) - удаляет атрибут с именем Name')
delattr(pt, "z")
print((pt.__dict__))

print("isinstance - позволяет проверить является ли екземпляр екземпляром класса pt, Ferst возвращает True или False ")
print(isinstance(pt, Ferst))

print("------------------------------------------")

class RRR:
    r = 7
    t = 8

qasw = RRR()
print(qasw.__dict__)
setattr(qasw, "z", 7)
print(qasw.z, qasw.r, qasw.t)


