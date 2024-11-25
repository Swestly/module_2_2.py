fenics = int(input('Введите первое число: '))
sec = int(input('Введите второе число: '))
srih = int(input('Введите третье число: '))
if fenics == sec and fenics == srih:
    print('Все', 3, 'числа равны между собой')
elif fenics== sec or fenics == srih or fenics == srih:
    print(2, 'числа равны между собой')
else:
    print('Обнаружено', 0, 'равных между собой чисел')
