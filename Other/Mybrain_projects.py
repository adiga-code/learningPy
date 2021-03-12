#Программы,которые предстоит мне сделать

#Нормальный калькулятор с интерфейсом
#Змейка
#Тетрис
#Игру, где нужно угадать число, загаданное компьютером

#Сумма натуральных чисел в заданном диапазоне. Дата: ?
num = []
for value in range(1,3002):
	num.append(value)

print(sum(num))

#Игра где нужно угадать число, загаданное компьютером. Дата: 5.12.2020г.
import random
from random import randint
#Генерируем число
number = random.randint(1,10001)
print("Let's go!!!")
#Просим ввести число
def rand_number() :
    what = int(input('\tВведите число: '))
#Выводим результат при разных значениях
    if what < number:
        print('Больше')
        rand_number()
    elif what > number:
        print('Меньше')
        rand_number() 
    else:
        print('You win!')
rand_number()
