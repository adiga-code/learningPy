#Переменные
message = "Hello,world!"
print(message)

#"Расширенная версия"
message = "Hello,world!"
print(message)
message = "Hello,Python world"
print(message)

#Изменение регистра символов

#Метод title образует первый символ каждого слова в строке к верхнему регистру(заглавными буквами 1-е символы)
name = "damir hejev"
print(name.title())

#Метод upper преобразует все символы строки к верхнему регистру
name = "Damir Hejev"
print(name.upper())

#Метод lower преобразует все символы строки к нижнему регистру
name = "Damir Hejev"
print(name.lower())

#Использование переменных в строках

#"Объединение Имени и Фамилии,которые хранятся в разных переменных"
first_name = "Damir"
second_name = "Hejev"
full_name = f"{first_name} {second_name}"
print(full_name)

#Более сложный пример с f строками
first_name = "Damir"
second_name = "Hejev"
full_name = f"{first_name} {second_name}"
print(f"Hello, {full_name.title()}!")

#Такой же пример с f строками, но сообщение сохраняется в переменной,потом выводится на экран
first_name = "Damir"
second_name = "Hejev"
full_name = f"{first_name} {second_name}"
message = f"Hello, {full_name.title()}!"
print(message)

#Табуляции и разрывы строк

#Табуляция с помощью "\t"rint("Python")
print("\tPython")

#Разрывы строк с помощью "\n"
print("Languages:\nPython\nC++\nJavaC")

#Удаление пропусков

#Удаление пропусков(слева и справа)
favorite_language = " python "
favorite_language = favorite_language.lstrip()
favorite_language = favorite_language.rstrip()
print(favorite_language)

#Использование апострова в переменной
print("One of Python's strengths is its divers community.")

#Выражения с числами(простейшие)
print( 3 - 2)
print( 3 + 2)
print( 3 / 2)
print( 3 * 2)
print( 3 ** 2)

#Выражения с числами(вещественные)
print(0.1 + 0.2)
print(0.1 - 0.2)
print(0.1 / 0.2)
print(0.1 * 0.2)
print(0.1 ** 0.2)

#Процесс получения вещественного числа при какой-то операции с целым
print(1 + 0.2)
print(1 - 0.2)
print(1 / 0.2)
print(1 * 0.2)
print(1 ** 0.2)

#Группировка чисел многозначного числа нижними подчеркиваниями чтобы оно лучше читалось
million = 14_000_000
print(million)

#Множественное присваивание(нескольким переменным несколько значений)
x, y, z = 1, 4, 0
print(x, y, z)

#Константы-переменные,которые не изменяются на протяжении всего срока жизни программы
KONSTANT = 5000
print(KONSTANT)

#Списки

#Простой список
spisok_bykes = ["trek", "cannondale", "redline", "specialized"]
print(spisok_bykes)

#Обращение к элементам списка(по отдельности)
spisok_bykes = ["trek", "cannondale", "redline", "specialized"]
print(spisok_bykes[0])

#При желании можно использовать строковые методы
spisok_bykes = ["trek", "cannondale", "redline", "specialized"]
print(spisok_bykes[0].title())

#Индексы начинаются с нуля , а не с 1
spisok_bykes = ["trek", "cannondale", "redline", "specialized"]
print(spisok_bykes[1])

#Если список длинный и нужно обратиться к конечным значениям нужно написать - .Например,чтобы обратиться к последнему надо написать -1
spisok_bykes = ["trek", "cannondale", "redline", "specialized"]
print(spisok_bykes[-1])

#Отдельные значения списка можно использовать в сообщениях с f строками
spisok_bykes = ["trek", "cannondale", "redline", "specialized"]
text = f"Hello, I like my {spisok_bykes[0]}"
print(text)

#Изменение списка
cars = ["BMW", "Mersedes", "Audi"]
print(cars)
cars[2] = "Porshe"
print(cars)

#Присоединение элементов в конце спика с помощью метода append
cars = ["BMW", "Mersedes", "Audi"]
print(cars)
cars.append('Porshe') 
print(cars)

#Так можно из пустого списка создать большой(добавлять в него значения)
cars = []

cars.append('BMW') 
cars.append('Mersedes') 
cars.append('Audi') 
cars.append('Porshe') 
print(cars)

#Вставка элемента в любое место списка с помощью метода insert
cars = ["BMW", "Mersedes", "Audi"]
print(cars)
cars.insert(2, 'Porshe') 
print(cars)

#Удаление элемента из списка с использованием команды del
cars = ["BMW", "Mersedes", "Audi"]
print(cars)
del cars[1]
print(cars)


#Удаление элемента из списка с использованием метода pop() он удаляет последнее значение из списка
cars = ["BMW", "Mersedes", "Audi"]
print(cars)

popped_car = cars.pop()
print(cars)
print(popped_car)

#Практическое применение метода pop()
cars = ["BMW", "Mersedes", "Audi"]

last_owned = cars.pop()
print(f"The last car I owned was a {last_owned.title()}")
#Извлечение элементов из произвольной позиции списка с помощью pop()
cars = ["BMW", "Mersedes", "Audi"]

last_owned = cars.pop(1)
print(f"The last car I owned was a {last_owned.title()}")

#Удаление элементов по значению с помощью remove()
cars = ["BMW", "Mersedes", "Audi"]
print(cars)
cars.remove("Mersedes")
print(cars)

#remove() можно использовать для работы со значением,которое удаляется из списка
cars = ["BMW", "Mersedes", "Audi"]
print(cars)

too_expensive = "Audi"
cars.remove(too_expensive)
print(cars)
print(f"\nA {too_expensive.title()} is too too expensive for me.")

#Сортировка списка в алфавитном порядке
motorcycles = ["Yamaha", "Ducati", "Honda", "Suzuki"]
motorcycles.sort()
print(motorcycles)

#Сортировка списка в обратном алфавитном порядке
motorcycles = ["Yamaha", "Ducati", "Honda", "Suzuki"]
motorcycles.sort(reverse=True)
print(motorcycles)

#Сортировка списка в алфавитном порядке
motorcycles = ["Yamaha", "Ducati", "Honda", "Suzuki"]

print(f"This is original list of motorcycles:")
print(motorcycles)

print(f"This is sorted list of motorcycles:")
print(sorted(motorcycles))

print(f"This is original list of motorcycles again:")
print(motorcycles)

#Вывод списка в обратном порядке
motorcycles = ["Yamaha", "Ducati", "Honda", "Suzuki"]
print(motorcycles)

motorcycles.reverse()
print(motorcycles)

#Определение длины списка
motorcycles = ["Yamaha", "Ducati", "Honda", "Suzuki"]
print(len(motorcycles))



#Работа со списками

#Перебор всего спика с помощью цикла for
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

#Более сложный пример с выводом сообщения для каждого фокусника
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

#Включение второй строки для каждого фокусника и красивое отображение посланий
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick {magician.title()}.\n")

#Выполнение действий после цикла for
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick {magician.title()}.\n")

print("Good job magicians!")

#Предотвращение ошибок с отступами в циклах

#Пропущенный отступ. Команда print должна иметь отступ.
magicians = ["alice", "david", "carolina"]
for magician in magicians:
print(magicians)

#Пропущенные отступы в других строках.Цикл для второго сообщения не применился(применился только к одному),т.к нет отступов
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
print(f"Good job {magician.title()}!")

#Лишние отступы.Нельзя ставить отступы там,где он не нужен.В данном случае выдаёт ошибку
text = "Hello Python world!"
    print(text)

#Лишние отступы после цикла.Т.к. строка имеет отступ, сообщение будет продублировано для каждого пользователя 
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"Good job {magician.title()}!")

    print("Thank you everyone")

#Пропущенное двоеточие. Двоеточие в конце команды for сообщает питону, что следующая строка является началом списка
magicians = ["alice", "david", "carolina"]
for magician in magicians
    print(magician)

#Создание числовых списков

#Функция range().В этой функции смещает на 1 так же как и при работе с индексами
for value in range(1,6):
    print(value)

#Если вместо (0,6) указать (6), то выведется числа от 0 до 5 
for value in range(6):
    print(value)

#Создание числовых списков с помощью list() и range()
numbers = list(range(1,6))
print(numbers)

#Построение списка четных чисел от 0 до 10
numbers = list(range(0,11,2))
print(numbers)

#Возведение чисел во 2 степень от 1 до 10
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

#То же самое, но компактнее
squares = []
for value in range(0,11):
    squares.append(value**2)

print(squares)

#Простая статистика с числовыми списками
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(num))

print(max(num))

print(sum(num))

#Генераторы списков. Он позволяет сгенерировать список всего в одной строке
squares = [value**2 for value in range(1,11)]
print(squares)


#Работа с частью списка.Сегменты


#Выведение первых трех элементов списка
players = ["Damir", "Darina", "Disana", "Dabek", "Papa"]
print(players[0:3])

#В сегментах индексы смещаются на 1
players = ["Damir", "Darina", "Disana", "Dabek", "Papa"]
print(players[1:4])

#Если начальный индекс не указан, то автоматически начинает сегмент с начала списка
players = ["Damir", "Darina", "Disana", "Dabek", "Papa"]
print(players[:4])

#Если не указать последний индекс, автоматически заканчивает сегмент в конце, начиная с указанного индекса
players = ["Damir", "Darina", "Disana", "Dabek", "Papa"]
print(players[2:])

#В сегментах работает отрицательный индекс. Чтобы вывести последние 3 игрока нужно написать индекс -3
players = ["Damir", "Darina", "Disana", "Dabek", "Papa"]
print(players[-3:])

#Если присутствует 3-ий индекс, то он указывает, сколько элементов нужно пропускать в заданном диапазоне
players = ["Damir", "Darina", "Disana", "Dabek", "Papa"]
print(players[0:3:2])

#Перебор содержимого сегмента с помощью цикла for
players = ["damir", "darina", "disana", "dabek", "papa"]

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#Копирование спика с использованием сегмента и изменение копии
my_foods = ["pizza", "cake", "shashlik"]
friend_foods = my_foods[:]

my_foods.append("ice cream")
friend_foods.append("chiken")

print("My favorite food are:")
print(my_foods)

print("\nMy friend's favorite food are:")
print(friend_foods)



#Кортежи. Это списки , которые нельзя изменить.Он выглядит как список, но вместо квадратных скобок присутствуют круглые.
numbers = (200,50)
print(numbers[0])
print(numbers[1])

#Кортеж определяется наличием запятой. Т.е. если в кортеже только одно значение, то после него нужно поставить запятую
numbers = (2,)

#Перебор всех значений в кортеже с помощью цикла for
numbers = (200,50)
for number in numbers:
    print(number)

#Изменение кортежа. Изменить отдельное значение кортежа нельзя, но переписать/изменить весь кортеж можно
numbers = (200,50)

print("Original numbers:")
for number in numbers:
    print(number)

numbers = (300,60)
print("\nModified numbers")
for number in numbers:
    print(number)



#Команды if

#Простой пример
cars = ["bmw", "mersedes", "audi", "subaru"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

#Проверка неравенства. Обозначения неравенства :  !=
pizza_dopping = 'mushrooms'
if pizza_dopping !="anchovies":
    print("Hold the anchovies")

#Сравнение чисел с помощью if и !=
answer = 17
if answer != 42:
    print("That is not correct answer.Please try again")

#Проверка равенства

#True
>>> car = "bmw"
>>> car == "bmw"
True

#False
>>> car = "bmw"
>>> car == "audi"
False

#Проверка равенства без учета регистра. False
>>> car = "Audi"
>>> car == "audi"
False

#True
>>> car = "Audi"
>>> car.lower() == "audi"
True

#Сравнения чисел. True
>>> age = 18
>>> age == 18
True

#False
>>> age = 18
>>> age == 44
False

#Команды меньше, больше, равно и т.д.
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False

#Использование and для проверки нескольких условий
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True

#Использование or для проверки нескольких условий
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False

#Проверка вхождения значений в список
>>> my_animals = ["Bobik", "Reksik", "Kisha"]
>>> "Bobik" in my_animals
True
>>> "Tiger" in my_animals
False

#Проверка отсутствия значения в списке с помощью not
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

#Логические выражения, они используются для проверки некоторых условий
game_active = True
can_edit = False


#Команды if. Подробнее
age = 19
if age >= 18:
    print("You are old enough to vote")

#Эта команда может содержать сколько угодно строк кода
age = 19
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet")

#Команды if-else
age = 17
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you tuurn 18!")

#Цепочки if-elif-else
age = 12
if age < 4:
    print("Your admission cost is 0 euro")
elif age < 18:
    print("Your admission cost is 25 euro")
else:
    print("Your admission cost is 45 euro")

#Более компактное решение
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 45
print(f"Your admission cost is {price} euro")

#Можно сколько угодно раз использовать elif
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 50:
    price = 45
else:
    price = 20
print(f"Your admission cost is {price} euro")

#Можно не использовать else, вместо него можно использовать elif
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 50:
    price = 45
elif age >= 50 and age < 65:
    price = 30
elif age >= 65:
    price = 20
print(f"Your admission cost is {price} euro")

#Использование нескольких if , для проверки нескольких условий одновременно
reqested_toppings = ["mushrooms", "extra chees"]
if "mushrooms" in reqested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in reqested_toppings:
    print("Adding pepperoni.")
if "extra chees" in reqested_toppings:
    print("Adding extra chees.")
print("\nFinished making your pizza!")



#Использование команд if со списками

#Вернемся к пицерии, с помощью цикла выводим сообщение, если нету топпинга, применяем if-else
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we don't have this topping right now.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")

#Проверка наличия элементов в списке. То же , что и в предыдущем примере, но если нет топпингов, выводится сообщение об обычной пицце
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Множественные списки. Если в списке не будет заказанного. Что делать?
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                                               'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry we don't have {requested_topping}")
print("\nFinished making your pizza!")




#Словари 

#Простой словарь
alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])

#Обращение к значениям в словаре
alien_0 = {'color': 'green', 'point': 5}
new_point = alien_0['point']
print(f"You just earned {new_point} points!")

#Добавление новых пар "ключ-значений" к словарю
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

#Создание пустого словаря и добавление пар "ключ-значений" в него
alien_0 = {}
alien_0['color'] = 'green'
alien_0['point'] = 5
print(alien_0)

#Изменение значений в словаре
alien_0 = {'color': 'green'}
print(f"My favorite color is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"My favorite color is {alien_0['color']}")

#Отслеживание скорости пришельца
alien_0 = {'x-position': 0, 'y-position': 25, 'speed': 'normal'}
print(f"Original position: {alien_0['x-position']}")
#Пришелец перемещается вправо
#Вычисляем текущую скорость
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'normal':
    x_increment = 2
else:
    #Высокая скорость пришельца
    x_increment = 3
#Новая позиция равна сумме старой и приращения
alien_0['x-position'] = alien_0['x-position'] + x_increment
print(f"New position: {alien_0['x-position']}")

#Удаление пар ключ значений из словаря
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
del alien_0['point']
print(alien_0)

#Словарь с однотипными ответами.Можно писать пары "ключ-значений" в столбик
favorite_languages = {
    'damir': 'python',
    'darina': 'c',
    'disana': 'java',
    'dabek': 'js',
    }
language = favorite_languages['damir'].title()
print(f"Damir's favorite language is {language}")

#Применение get().get() можно использовать если "ключ-значения" в словаре нет
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('point', 'No point value assigned.')
print(point_value)

#Перебор всех пар "ключ-значений" с помощью for и items()
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f'Value: {value}')

#Изменить программу имен-любимыx языков, с помощью for и items()
favorite_languages = {
    'damir': 'python',
    'darina': 'c',
    'disana': 'java',
    'dabek': 'js',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#Применение метода key(), для вывода "ключей" без их значений(упрощает прочтение кода)
favorite_languages = {
    'damir': 'python',
    'darina': 'c',
    'disana': 'java',
    'dabek': 'js',
    }
for name in favorite_languages.keys():
    print(name.title())

#Применение команды if с циклом for
favorite_languages = {
    'damir': 'python',
    'darina': 'c',
    'disana': 'java',
    'dabek': 'js',
    }
friends = ['darina', 'dabek']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name.title()}, I see you like {language.title()}")

#Методом keys(), можно узнать, участвовал ли участник в опросе
favorite_languages = {
    'damir': 'python',
    'darina': 'c',
    'disana': 'java',
    'dabek': 'js',
    }
if 'papa' not in favorite_languages.keys():
    print('Papa, please vote') 

#Перебор ключей в определенном порядке. Функция sort() для "ключей"
favorite_languages = {
    'damir': 'python',
    'darina': 'c',
    'disana': 'java',
    'dabek': 'js',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for vote")

#СОртировка значений с помощью for и values()
favorite_languages = {
    'damir': 'python',
    'darina': 'c',
    'disana': 'java',
    'dabek': 'js',
    }
print("Your favorite languages:")
for language in favorite_languages.values():
    print(language)

#Проверка значения на уникальность, с помощью set()
favorite_languages = {
    'damir': 'python',
    'darina': 'c',
    'disana': 'java',
    'dabek': 'java',
    }
print("Your favorite languages:")
for language in set(favorite_languages.values()):
    print(language.title())

#Нельзя путать множества с словарями.Если нет пар "ключ-значений" ,то это множество
languages = {'python', 'ruby', 'js', 'c'}
print(languages)

#Создание списка словарей
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#Применение цикла for с списком со словарями. Или автоматическое создание пришельцев
#Создание пустого списка для хранения пришельцев.
aliens = []
#Создание 30 пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#Вывод первых пяти пришельцев
for alien in aliens[:5]:
    print(alien)
#Вывод количества созданных пришельцев
print(f'Total nummber of aliens : {len(aliens)}')

#Изменение цвета 3 пришельцев.Работа со множеством
#Создание пустого списка для хранения пришельцев.
aliens = []
#Создание 30 пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#Изменение первых 3 пришельцев
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
#Вывод первых 5 пришельцев
for alien in aliens[:5]:
    print(alien)

#Применение цепочки if-elif
#Создание пустого списка для хранения пришельцев.
aliens = []
#Создание 30 пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#Изменение первых 3 пришельцев
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['point'] = 15
        alien['speed'] = 'fast'
#Вывод первых 5 пришельцев
for alien in aliens[:5]:
    print(alien)

#Список в словаре
#Сохранение информации о заказанной пицце
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
#Описание заказа
print(f"You ordered a {pizza['crust']}-crust pizza")
for topping in pizza['toppings']:
    print("\t" + topping)

#Вложение списка в словарь
favorite_languages = {
    'damir': ['python','ruby'],
    'darina': ['c', 'c++'],
    'dabek': ['c#'],
    'disana': ['java', 'javascript'],
    }
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#Применение команды if к этому примеру
favorite_languages = {
    'damir': ['python','ruby'],
    'darina': ['c', 'c++'],
    'dabek': ['c#'],
    'disana': ['java', 'javascript'],
    }
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is:")
    else:
        print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#Словарь в словаре
users = {
    'damir': {
        'first': 'damir',
        'second': 'hejev',
        'location': 'baksan',
        },
    'darina': {
        'first': 'darina', 
        'second': 'hejeva',
        'location': 'nalchik'
        },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{user_info['first']} {user_info['second']}"
    location = user_info['location']
    print(f"Full name: {full_name.title()}")
    print(f"Location: {location.title()}")





#Функция input()

#Простая программа с использованием функции input()
message = input("Tell me something:")
print(message)

#Нужно писать содержательные подсказки, чтобы было понятно что писать
name = input("Please, tell me your name: ")
print(f'\nHello, {name}!')

#Что делать если подсказка занимает более одной строки?
message = 'We want your name.'
message += '\nWhat is your first name? '
name = input(message)
print(f"Hello, {name}")

#Получение числового ввода с помощью int(), и проверка на "число"
age = input('How old are you? ')
age = int(age)
print(age)
if 8 > age:
    print('Ok')
else:
    print('Yes')

#Ещё один пример
height = input("How tall are you? ")
height = int(height)
if height >= 48:
    print("\nEnough, welcome")
else:
    print("\nYou are little")

#Оператор вычисления остатка %
>>> 4 % 3
1
>>> 5 % 2
1
>>> 6 % 3
0

#Как можно использовать %.Для определения четности введенного числа
number = input('Введите число для определения четности:')
number = int(number)
if number % 2 == 0:
    print(f'\nЧисло {number} четное')
else:
    print(f'\nЧисло {number} нечетное')




#Циклы while

#Простой пример
number = 1
while number <= 5:
    print(number)
    number += 1

#Для прерыва работы программы
prompt = '\nTell me something , and I will repeat it back to you'
prompt += '\nEnter "quit" to end the program.'
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

#Применение if для не выведении слова для остановки цикла 
prompt = '\nTell me something , and I will repeat it back to you'
prompt += '\nEnter "quit" to end the program.'
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

#Флаги. Для сообщения программе, выполнится ли программе далее
prompt = '\nTell me something , and I will repeat it back to you'
prompt += '\nEnter "quit" to end the program.'
message = ''
active = True
while active == True:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#Тоже самое, но с помощью команды break
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to Baksan")

#Команда continue, продолжение цикла
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#Предотвращение зацикливания, чтобы цикл не выполнялся бесконечно
x = 1
while x <= 5:
    print(x)
    x += 1

#Бесконечный цикл
x = 1
while x <= 5:
    print(x)

#Перемещение элементов между списками
#Делаем 2 списка: пользователей для проверки
#и пустой список для проверенных пользователей.
uncorfirmed_users = ['darina', 'damir', 'disana']
confirmed_users = []
#Проверяем пользователей, пока остаются непроверенные.
#Каждый проверенный пользователь перемещается в 
#соответствующий список
while uncorfirmed_users:
    current_user = uncorfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
#Вывод всех проверенных пользователей
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Применение функции remove() в циклах while
pets = ['cat', 'tiger', 'dog', 'cat', 'lion', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#Заполнение словаря данными, введеными пользователем
responses = {}
#Установка флага для продолжения опроса
polling_active = True
while polling_active:
    #Запрос имени и ответа пользователя
    name = input("\nУкажите ваше имя: ")
    response = input("Какую гору ты хочешь покорить? ")
    #Сохраняем ответ в словаре
    responses[name] = response
    #Проверка продолжения опроса
    repeat = input("\nХотите заполнить анкету еще одного человека?(да/нет)")
    if repeat == 'нет':
        polling_active = False
#Выведение результатов после окончания опроса
print("\n---Результаты---")
for name,response in responses.items():
    print(f"{name.title()} хочет залесть на гору {response} ")





#Функции

#Простая функция
def greet_user():
    """Выводит сообщение"""
    print("Hello!")
greet_user()

#Передача информации функции
def greet_user(username):
    print(f"Hello, {username.title()}")
greet_user('damir')

#Позиционные аргументы
def describe_pet(animal_type, animal_name):
    print(f"This is {animal_type}, his name is {animal_name.title()}")
describe_pet('dog', 'bobik')

#Многкратные вызовы функций
def describe_pet(animal_type, animal_name):
    print(f"This is {animal_type}, his name is {animal_name.title()}")
describe_pet('dog', 'bobik')
describe_pet('dog', 'reksik')

#Именнованные аргументы функции
def describe_pet(animal_type, animal_name):
    print(f"This is {animal_type}, his name is {animal_name.title()}")
describe_pet(animal_type='dog', animal_name='bobik')

#Значения по умолчанию. Указываются для параметра, после можно изменить 
def describe_pet(animal_name, animal_type='dog'):
    print(f"This is {animal_type}, his name is {animal_name.title()}")
describe_pet(animal_name='bobik')
describe_pet(animal_name='reksik')
describe_pet('dgedu delya', 'cat')

#Стили вызова функций при значениях по умолчанию
def describe_pet(pet_name, animal_type = 'dog'):
    print(f"This is {animal_type}, his name is {pet_name.title()}.")
#Пес по имени Бобик
describe_pet('bobik')
describe_pet(pet_name = 'bobik')
#Кот по имени Джэду-делэ
describe_pet('dgedu-delya', 'cat')
describe_pet(pet_name = 'dgedu-delya', animal_type = 'cat')
describe_pet(animal_type = 'cat', pet_name = 'dgedu-delya')

#Предотвращение ошиюок в аргументах.При указании параметров без аргументов
def describe_pet(animal_name, animal_type='dog'):
    print(f"This is {animal_type}, his name is {animal_name.title()}")
describe_pet()

#Возвращение простого значения с помощью return
def get_formated_name(name, last_name):
    """Возвращаем аккуратно отформатированное полное имя."""
    full_name = f"{name.title()} {last_name.title()}"
    return full_name
musician = get_formated_name('Damir', 'hejev')
print(musician)

#Необязательные аргументы.
def get_formated_name(first_name , last_name , middle_name = ''):
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name
musician = get_formated_name('damir', 'hejev', 'krasava')
print(musician)
musician = get_formated_name('darina', 'hejeva')
print(musician)

#Возвращение словаря
def build_name(first_name , last_name , age = None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician =  build_name('damir', 'hejev', 78)
print(musician)

#Использование функции в цикле while
def get_formated_name(first_name , last_name ):
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name
while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' to quit")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formated_name = get_formated_name(f_name, l_name)
    print(f'Hello, {formated_name.title()}')

#Передача списка. Испрользование for и списков
def greet_users(names):
    for name in names:
        text = f"Hello, {name}!"
        print(text)
users = ['Damir', 'Darina', 'Disana']
greet_users(users)

#Изменение списка в функции
def print_models(unprinted_designs , completed_models):
    while unprinted_designs:
        current_users = unprinted_designs.pop()
        print(f"Printing model: \n\t{current_users}")
        completed_models.append(current_users)
def show_completed_models(completed_models):
    print("Printed models:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['dabek', 'robot', 'cube']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Чтобы не изменять весь список в функции, можно при вызове аргумента
#скопировать весь спико и применить копию
name_function(name_spisok[:])

#Передача произвольного количества аргументов функции, с помощью *
def make_pizza(*toppings):
    print(f"\n\t{toppings}")
make_pizza('грибы')
make_pizza('грибы', 'молюски' , 'листья салата')

#Позиционные и произвольные аргументы
def make_pizza(size, *toppings):
    print(f"\nMaked pizza size - {size}, with your toppings")
    for topping in toppings:
        print(topping)
make_pizza(15, 'грибы')
make_pizza(12, 'грибы', 'молюски' , 'листья салата')

#использование произвольного набора именнованных аргументов , с созданием словаря
def build_profile(first , last , **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('damir', 'hejev',
                             location = 'baksan',
                             profechiom = 'student')
print(user_profile)

#Импортирование модуля/функции из другой программы
import name_module

name_module.function(arguments)

#Импортирование конкретных функций из модуля
from name_module import name_function

name_function(arguments)

#Назначение псевдонима для функции в модуле
from name_module import name_function as psevdoname_function

psevdoname_function(arguments)

#Назначение псевдонима для всего модуля
import name_module as psevdoname_module

psevdoname_module.name_function(arguments)

#Импортирование всех функций модуля
from name_module import *

name_function(arguments)





#кЛАССЫ. Класс Dog. Метод __init__.Создание экземпляра класса



#Обращение к атрибутам
class Dog():
    """Простая модель собаки"""
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting. ")

    def roll_over(self):
        print(f"{self.name} roll over! ")

"""Создаём экземпляр класса"""      
my_dog = Dog("Dgek", 11)
your_dog = Dog("Bobik", 3)
"""Обращение к атрибутам"""
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age}.")

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age}")

"""Вызов методов"""
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()




#Назначение атрибуту значения по умолчанию
class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        self.make = make            
        self.model = model
        self.year = year
        self.read_odometer = 0
    def odometr_reading(self):
        """Выводит пробег машины"""
        print(f"This car has {self.read_odometer} kilometers on it")
    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
car_bmw = Car("BMW", "M5", 2021)
print(car_bmw.get_descriptive_name())
car_bmw.odometr_reading()




#Изменение значений атрибута




#Прямое изменение значения атрибута
class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        self.make = make            
        self.model = model
        self.year = year
        self.odometr_reading = 0
    def read_odometer(self):
        """Выводит пробег машины"""
        print(f"This car has {self.odometr_reading} kilometers on it")
    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
car_bmw = Car("BMW", "M5", 2021)
print(car_bmw.get_descriptive_name())
car_bmw.read_odometer()
#Прямое изменение значения атрибута
car_bmw.odometr_reading = 23
car_bmw.read_odometer()




#Изменение значения атрибута с использованием метода(функции)
class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        self.make = make            
        self.model = model
        self.year = year
        self.odometr_reading = 0
    def read_odometer(self):
        """Выводит пробег машины"""
        print(f"This car has {self.odometr_reading} kilometers on it")
    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    def update_odometr(self, number):
        """Устанавливает заданное значение на одометре"""
        """Проверяется изменение одометра в обратную сторону"""
        if number >= self.odometr_reading:
            self.odometr_reading = number
        else:
            print("You can't roll back an odometr")
car_bmw = Car("BMW", "M5", 2021)
print(car_bmw.get_descriptive_name())
car_bmw.read_odometer()
#Изменение значения одометра
car_bmw.update_odometr(33_000)
car_bmw.read_odometer()
#Повторное изменения значения для проверки на изменение его значения"""
car_bmw.update_odometr(10_000)
car_bmw.read_odometer()




#Изменение значения атрибута с приращением
class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        self.make = make            
        self.model = model
        self.year = year
        self.odometr_reading = 0
    def read_odometer(self):
        """Выводит пробег машины"""
        print(f"This car has {self.odometr_reading} kilometers on it")
    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    def update_odometr(self, number):
        """Устанавливает заданное значение на одометре"""
        """Проверяется изменение одометра в обратную сторону"""
        if number >= self.odometr_reading:
            self.odometr_reading = number
        else:
            print("You can't roll back an odometr")
    def increment_odometr(self, kilometers):
        self.odometr_reading += kilometers
car_bmw = Car("BMW", "M5", 2021)
print(car_bmw.get_descriptive_name())
car_bmw.read_odometer()
#Изменение значения одометра
car_bmw.update_odometr(33_000)
car_bmw.read_odometer()
#Увеличение показания одометра методом"""
car_bmw.increment_odometr(20_000)
car_bmw.read_odometer()

#Наследование



#Метод __init__ класса потомка, вызов метода родительского класса методом super()
class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometr(self):
        print(f"This car has {self.odometr_reading} kilometrs on it")
    def update_odometr(self, kilometrs):
        if kilometrs >= self.odometr_reading:
            self.odometr_reading = kilometrs
        else:
            print("You can't roll back an odometr!!!")
    def increment_odometr(self, kilometr):
        self.odometr_reading += kilometr
class ElectricCar(Car):
    """Представляет аспекты машин, специфические для электрокаров"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())




#Определение атрибутов методов класса-потомка
class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometr(self):
        print(f"This car has {self.odometr_reading} kilometrs on it")
    def update_odometr(self, kilometrs):
        if kilometrs >= self.odometr_reading:
            self.odometr_reading = kilometrs
        else:
            print("You can't roll back an odometr!!!")
    def increment_odometr(self, kilometr):
        self.odometr_reading += kilometr
class ElectricCar(Car):
    """Представляет аспекты машин, специфические для электрокаров"""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля
        """
        super().__init__(make, model, year)
        self.battery_size = 75
    def describe_battery(self):
        """Выводит сообщение о мощности аккумулятора"""
        print(f"This car has {self.battery_size}-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()



#Переопределение методов класса-родителя
class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometr(self):
        print(f"This car has {self.odometr_reading} kilometrs on it")
    def update_odometr(self, kilometrs):
        if kilometrs >= self.odometr_reading:
            self.odometr_reading = kilometrs
        else:
            print("You can't roll back an odometr!!!")
    def increment_odometr(self, kilometr):
        self.odometr_reading += kilometr
class ElectricCar(Car):
    """Представляет аспекты машин, специфические для электрокаров"""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля
        """
        super().__init__(make, model, year)
        self.battery_size = 75
    def describe_battery(self):
        """Выводит сообщение о мощности аккумулятора"""
        print(f"This car has {self.battery_size}-kWh battery.")
    def fill_gas_tank(self):
        """У электромобилей нет бензобака"""
        print("This car don't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()





#Использование экземпляров как атрибуты.

class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometr(self):
        print(f"This car has {self.odometr_reading} kilometrs on it")
    def update_odometr(self, kilometrs):
        if kilometrs >= self.odometr_reading:
            self.odometr_reading = kilometrs
        else:
            print("You can't roll back an odometr!!!")
    def increment_odometr(self, kilometr):
        self.odometr_reading += kilometr
class Battery():
    """Простая модель аккумулятора автомобиля"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит сообщение о мощности аккумулятора"""
        print(f"This car has {self.battery_size}-kWh battery.")
    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size == 75:
            range = 260
        if self.battery_size == 100:
            range = 315
        print(f'This car can go about {range} miles on a full charge')
class ElectricCar(Car):
    """Представляет аспекты машин, специфические для электрокаров"""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        """У электромобилей нет бензобака"""
        print("This car don't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
        








