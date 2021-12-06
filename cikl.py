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
vib = input('если конец то жми y, если добавить человека то жми n')

while True:
    if vib == 'n':
        print('введите данные человека')
        dch = input('имя и фамилию:')
        vib = input('если конец то жми y, если добавить человека то жми n')
    else:
        print('конец')
        break