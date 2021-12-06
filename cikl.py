# WHILE
psw = input('psw')
while True:
    if len(psw) < 8:
        print('меньше 8 символов')
    else:
        print('всё верно')
        break
    psw = input('psw')

print('введите данные человека')
dch = input('имя и фамилию:' )
vib = input('если конец то жми y, если добавить человека то жми n ')

while True:
    if vib == 'n':
        print('введите данные человека 6')
        dch = input('имя и фамилию 3:')
        vib = input('если конец то жми y, если добавить человека то жми n ')
    else:
        print('конец')
        break

## CONTINUE ПРИМЕР
s = 0; i = -5

while i < 4:
    i = i + 1
    if i == 0:
        continue
        print("этого не будет видно")
    print(i)

print(s)

######################  FOR
# for <переменная> in <список>:
#     операторы 1 ...N
print("--------------------")
for x in 1, 5, 2, 4:
    print(x**2)
print("range(start, stop, step)----только целые числа----------------")
for x in range(1, 5, 1):
    print(x)

print("---------список-----------")
k = 0.5
b = 2
lst = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
for x in lst:
    print(x*k+b)

g = input('слово или символ:' )
for x in range(0, 5, 1):
    print(g)

print('вложенный цикл for')
a = [ [1, 2, 3], [4, 5, 6] ]
n = 2
m = 3
for x in range(n):
    for i in range(m):
        print(a[x] [i], end='')
    print()





