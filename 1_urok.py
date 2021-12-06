#start

# объединение происходит только так
d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}

d1.update(d2)
print(d1)

vasa = {1: 11, 2: 14}
print(vasa)
red = {3: 13, 4: 14}
print(red)
vasa.update(red)
print(vasa)

class Poin:
    cou = 0

pt = Poin()
# статические поведение класса
print(pt.cou)
Poin.cou = 10
print(pt.cou)
# не статическое свойство
pt.cou = 12
print(pt.cou)