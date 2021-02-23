# Nom 2.3

#1) Сохранение имени пользователя в переменной и выведение
name = "Dabek"
print(f"{name}, what's your name? ")

# Nom 2.4

#1) Капитализация первых букв каждого слова
name = "very big summer"
print(f"{name.title()} is hot ")
#2) Сохранить слово-слова в нижнем регистре и вывести
name = "Very Big Summer"
print(f"{name.lower()} is hot ")
#3) Сохранить слово-слова в верхнем регистре и вывести
name = "Very Big Summer"
print(f"{name.upper()} is hot ")

# Nom 2.5

#1) Вывести умную фразу умного человека
print(f'Damir Hejev once said,"Peoples are clever,because Damir is good!"')

# Nom 2.6

#1) Вывести умную фразу, но перед этим сохранить все фразы в переменных
name = "Damir Hejev"
clever_fraza = '"Peoples are clever,because Damir is good!"'
print(f'{name} once said, {clever_fraza}')

# Nom 2.7

#1) Применить lstrip(),rstrip(),strip() и + табуляции и разрывы строк
name = " Damir "
name = name.lstrip()
name = name.rstrip()
name = name.strip()
print(f"Names:\n {name},\nDisana,\nDarina,\nDabek\n \tHejevi")

# Nom 2.8

#1) Написать операции сложения,умножения,вычитания,деления
print(4 + 4)
print(12 - 4)
print(16 / 2)
print(2 * 4)

# Nom 2.9

#1) В сообщение добавить число взяв его из переменной и вывести
favorite_number = 9
text = f"My favorite number is {favorite_number}"
print(text)

# Nom 2.10

#1)Нужно добавить комментарий к скрипту
#Но я практиковал это много раз;)



#Списки

# Nom 3.1

#1)Создать список с именами и вывести имя каждого по отдельности
names = ["Disana", "Darina", "Damir", "Dabek"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Nom 3.2

#1)Вывести сообщения с использованием имен из задачи 3.1
names = ["Disana", "Darina", "Damir", "Dabek"]
print(f"Hello,this is {names[0]}")
print(f"Hello,this is {names[1]}")
print(f"Hello,this is {names[2]}")
print(f"Hello,this is {names[3]}")

# Nom 3.3

#1)Создать список с примерами сроками и т.д.
cars = ["BMW", "Mersedes", "Audi"]
print(f"{cars[0]} is the best car forever")
print(f"{cars[1]} is the good car,but {cars[0]} is the best ")
print(f"{cars[2]} is a very good car, better that {cars[1]} ,but {cars[0]} is the best")

# Nom 3.4

#1)Сделайте список гостей и напишите каждому приглашение
peoples = ["Disana", "Darina", "Dabek", "Damir"]

print(f"Welcome, {peoples[0]} I have food")
print(f"Hello, {peoples[1]} what do you mean about food?Welcome")
print(f"{peoples[2]} come here")
print(f"{peoples[-1]} ;)")

# Nom 3.5

#1)Закончить начатое в Nom 3.4 заменить одного гостя другим,извиниться всем и вывести
peoples = ["Disana", "Darina", "Dabek", "Damir"]

print(f"Welcome, {peoples[0]} I have food")
print(f"Hello, {peoples[1]} what do you mean about food?Welcome")
print(f"{peoples[2]} come here")
print(f"{peoples[-1]} ;)")

print(f"Friends, {peoples[2]} don't want to eat")

peoples.append("Mama")
print(f"Welcome, {peoples[-1]} I am your son")

# Nom 3.6

#1)Из упражнения 3.5, добавить трех гостей вызовами insert() and append(), написать приглас-ную
peoples = ["Disana", "Darina", "Dabek", "Damir"]

print(f"Welcome, {peoples[0]} I have food")
print(f"Hello, {peoples[1]} what do you mean about food?Welcome")
print(f"{peoples[2]} come here")
print(f"{peoples[-1]} ;)")

print(f"Friends, {peoples[2]} don't want to eat")

peoples.append("Mama")
print(f"Welcome, {peoples[-1]} I am your son")

peoples.append("Nana")
peoples.insert(0, "Dada")
peoples.insert(3, "Papa")
print(f"Welcome, {peoples[0]} ")
print(f"Welcome, {peoples[3]} ")
print(f"Welcome, {peoples[-1]} ")

# Nom 3.5

#1)Закончить начатое в номере 3.6,т.е. удалить всех людей , чтобы осталось только 2,извиниться и удалить их командой del
peoples = ["Disana", "Darina", "Dabek", "Damir"]

print(f"Welcome, {peoples[0]} I have food")
print(f"Hello, {peoples[1]} what do you mean about food?Welcome")
print(f"{peoples[2]} come here")
print(f"{peoples[-1]} ;)")

print(f"Friends, {peoples[2]} don't want to eat")

peoples.append("Mama")
print(f"Welcome, {peoples[-1]} I am your son")

peoples.append("Nana")
peoples.insert(0, "Dada")
peoples.insert(3, "Papa")
print(f"Welcome, {peoples[0]} ")
print(f"Welcome, {peoples[3]} ")
print(f"Welcome, {peoples[-1]} ")

print("\nPeoples, I'm so sorry, but today I don't have food")

peoples_pop = peoples.pop()
print(f"\nI'm so sorry {peoples_pop}, but I don't have food")
peoples_pop = peoples.pop(0)
print(f"\nI'm so sorry {peoples_pop}, but I don't have food")
peoples_pop = peoples.pop(1)
print(f"\nI'm so sorry {peoples_pop}, but I don't have food")
peoples_pop = peoples.pop(2)
print(f"\nI'm so sorry {peoples_pop}, but I don't have food")
peoples_pop = peoples.pop(3)
print(f"\nI'm so sorry {peoples_pop}, but I don't have food")
peoples_pop = peoples.pop(-1)
print(f"\nI'm so sorry {peoples_pop}, but I don't have food")

print(f"\n{peoples[0]}, come here tomoroy")
print(f"{peoples[1]}, come here tomoroy")

del peoples[0]
del peoples[-1]

print(peoples)


#Сортировка списков

# Nom 3.8

#1)Использовать функцию sorted(), reverse(), sort()
countries = ["Russia", "UK", "KBR", "Germany", "USA"]

print(countries)
print(sorted(countries))

countries.reverse()
print(countries)

countries.reverse()
print(countries)

countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)

# Nom 3.9

#1)В одной из программ из упр. с 3.4-3.7 использовать len() и узнать количество людей приглашенных на вечеринку
peoples = ["Disana", "Darina", "Dabek", "Damir"]

print(f"Welcome, {peoples[0]} I have food")
print(f"Hello, {peoples[1]} what do you mean about food?Welcome")
print(f"{peoples[2]} come here")
print(f"{peoples[-1]} ;)")
print("\n")
print(len(peoples))

# Nom 3.10

#1)Применить все функции главы
cities = []
cities.append("Parish")
print(cities[0].title())
cities.append("London")
print(cities[1])
cities.append("Nalchik")
print(cities[2].title())
cities.append("Baksan")
print(cities[3])
cities.append("Kiev")
print(cities[-1])

print(f"{cities[2].title()} is the best city forever!")

cities[0] = "Piter"
print(' ')
print(cities[0].title())
print(cities[1].title())
print(cities[2].title())
print(cities[3].title())
print(cities[-1].title())

cities.insert(3, "Damirland")
print(cities)

del cities[3]
print(cities)

poped_cities = cities.pop(0)
print(f"{poped_cities} is not good")

print("This is countries list:")
print(cities)

print("This is sorted list:")
print(sorted(cities))

print("This is countries list again:")
print(cities)

print("Sorted list again")
cities.reverse()
print(cities)

print("Not sorted list again")
cities.reverse()
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

print(len(cities))



#Работа со списками

# Nom 4.1

#1)Вывести для каждого элемента списка сообщение, применяя цикл for и добавить в конце дополнительное сообщение
pizzas = ["Three cheez", "Assorti", "Margarite"]
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

print("\nI really love pizza!")

# Nom 4.2

#1)Сделать также как в упражнении 4.1, но вместо пиццы , будут животные
animals = ["Dog", "Lion", "Tiger"]
for animal in animals:
    print(f"I like {animal.title()}!")

print("\nI really love this animals!")



#Числовые списка

# Nom 4.3

#1)Использовать цикл for для вывода чисел от 1 до 20
for value in range(1,21):
    print(value)

# Nom 4.4

#1)Создать список чисел от 1 до 1000000(я создам от 1 до 50)) и вывести. Применил list
numbers = list(range(1,51))
print(numbers)

#1)Вывести тоже самое, но применить цикл for
numbers = []
for value in range(1,51):
    numbers.append(value)

print(numbers)

# Nom 4.5

#1)Создать список чисел от 1 до 1000000, воспользоваться функциями min() max() sum()
numbers = []
for value in range(1,51):
    numbers.append(value)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Nom 4.6

#1)Воспользоваться 3-им аргументом функции range() для создания списка нечетных чисел от 1 до 20(Нужно поставить пробел и написать 2)
for value in range(1,21, 2):
    print(value)

# Nom 4.7

#1)Создать список чисел кратных 3 , в диапазоне от 3 до 30 ивывести с помощью цикла for
numbers = [3, 12, 21, 30]
for number in numbers:
    print(numbers)

# Nom 4.8

#1)Создать список первых 10-ти кубов и вывести значения с помощью цикла for
cubes = []
for value in range(1,11):
    cubes.append(value**3)

print(cubes)

# Nom 4.9 

#1)Сделать тоже самое,что и в упражнении 4.8, но использовать конструкцию генератор(написать кратко)
cubes = [value**3 for value in range(1,11)]
print(cubes)


#Сегменты

# Nom 4.10

#1)Добавить в конец одной из программ главы фрагмент, который использует сегмент для вывода трех первых элементов списка
magicians = ["Alice", "David", "Carolina", "Damir"]
for magician in magicians:
    print(magician)

print("The irst three itens in the list are:")
print(magicians[0:3])

#2)Добавить в конец одной из программ главы фрагмент, который использует сегмент для вывода трех элементов из середины списка
magicians = ["Alice", "David", "Carolina", "Damir", "Dabek"]
for magician in magicians:
    print(magician)

print("The items from the middle of the list area:")
print(magicians[1:4])

#3)Добавить в конец одной из программ главы фрагмент, который использует сегмент для вывода трех элементов в конце списка
magicians = ["Alice", "David", "Carolina", "Damir", "Dabek"]
for magician in magicians:
    print(magician)

print("The irst three itens in the list are:")
print(magicians[2:])

# Nom 4.11

#1)Из упражнения 4.1 создать копию списка пицц и добавить  разные виды пиццы каждому из списков, вывести с помощью цикла for
pizzas = ["Three cheez", "Assorti", "Margarite"]
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

print("\nI really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append("Pepperoni")
friend_pizzas.append("Shashlik_pizza")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

# Nom 4.12

#1)Сделать тоже самое, что в упражнении 4.11, но использовать раннее написанную задачу из книги
my_foods = ["pizza", "cake", "shashlik"]
friend_foods = my_foods[:]

my_foods.append("ice cream")
friend_foods.append("chiken")

print("My favorite food are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite food are:")
for friend_food in friend_foods:
    print(friend_food)


#Кортежи 

# Nom 4.13

#1)Сохранить в кортеже меню ресторана из 5 блюд, вывести с помощью for, изменить кортеж(два блюда), снова вывести
foods = ("ice cream", "shashlik", "pizza", "lulya kebab", "plov")
print("This is our old menu:")
for food in foods:
    print(food.title())

foods = ("burger", "shashlik", "pizza", "lulya kebab", "macarons")
print("\nThis is our new menu:")
for food in foods:
    print(food.title())

# Nom 4.14

#1)Просмотреть руководство по стилю PEP 8 https://python.org/dev/peps/pep-0008/

# Nom 4.15

#1)Выбрать 3 программы написанные в этой главе, применить рекомендации PEP 8
numbers = (200,50)
print("Original numbers:")
for number in numbers:
    print(number)
numbers = (300,60)
print("\nModified numbers:")
for number in numbers:
    print(number)

#2)Вторая программа
my_foods = ["pizza", "cake", "shashlik"]
friend_foods = my_foods[:]
my_foods.append("ice cream")
friend_foods.append("chiken")
print("My favorite food are:")
print(my_foods)
print("\nMy friend's favorite food are:")
print(friend_foods)

#3)Третья программа
squares = []
for value in range(0,11):
    squares.append(value**2)
print(squares)



#Команды if

# Nom 5.1

#1)Написать последовательность условий, вывести.5 должно быть равно true, 5 = false
car = "bmw"
if car == car.title():
    print("True")
else:
    print("False")
#_________________________________
if car == "Audi":
    print("False")
else:
    print("True")
#_________________________________
if car == car.lower():
    print("False")
else:
    print("True")
#_________________________________
if car != "mersedes":
    print("True")
else:
    print("False")
#_________________________________
if car.upper() == "bmw":
    print("False")
else:
    print("True")
#_________________________________
car = 10
if car >= 13:
    print("True")
else:
    print("False")
#_________________________________
if car <= 15:
    print("True")
else:
    print("False")
#_________________________________
if car == 20:
    print("True")
else:
    print("False")
#_________________________________
if car <= 44:
    print("True")
else:
    print("False")
#_________________________________
if car == 14 or 9:
    print("False")
else:
    print("True")

# Nom 5.2

#1)Применить все условия из главы
car = "bmw"
number = 9
foods = ["pizza", "shashlik", "ice cream", "soup"]
if car == "audi":
    print("True")
else:
    print("False")
#______________________________________
if car == "bmw":
    print("True")
else:
    print("False")
#______________________________________
if car.upper() == "BMW":
    print("\nTrue")
else:
    print("False")
#______________________________________
if car.title() == "BMW":
    print("True")
else:
    print("False")
#______________________________________
if number == 9:
    print("\nTrue")
else:
    print("False")
#______________________________________
if number < 3:
    print("True")
else:
    print("False")
#______________________________________
if number > 8:
    print("True")
else:
    print("False")
#______________________________________
if number >= 54:
    print("True")
else:
    print("False")
#______________________________________
if number <= 9:
    print("True")
else:
    print("False")

number_2 = 88
if number == 9 and number_2 == 88:
    print("\nTrue")
else:
    print("False")
#_____________________________________
if number >= 4 and number_2 <= 45:
    print("True")
else:
    print("False")
#_____________________________________
if number == 7 or number_2 >= 9:
    print("\nTrue")
else:
    print("False")
#_____________________________________
if number >= 32 or number_2 == 95:
    print("True")
else:
    print("False")
#_____________________________________
if "Kasha" in foods:
    print("\nTrue")
else:
    print("False")
#_____________________________________
if "shashlik" in foods:
    print("True")
else:
    print("False")
#_____________________________________
if "shashlik" not in foods:
    print("\nTrue")
else:
    print("False")
#_____________________________________
if "macaron" not in foods:
    print("True")
else:
    print("False")

# Nom 5.3

#1)Написать команду if и вывести сообщение, если условие истинно
alien_color = "green"
if alien_color == "green":
    print("EEEEEBOOOOOY 5 points")

#2)Точно также, но условие не истино
alien_color = "green"
if alien_color == "red":
    print("EEEEEBOOOOOY 5 points")

# Nom 5.4

#1)Продолжить упр. 5.3, но если условие неверное, вывести, что заработано 10 очков
alien_color = "green"
if alien_color == "red":
    print("EEEEEBOOOOOY 5 points")
else:
    print("EEEEEBOOOOOY 10 points")

# Nom 5.5

#1)Продолжить упр. 5.4, приенить if-elif-else , вывести сообщение для каждой ситуации
alien_color = "red"
if alien_color == "red":
    print("EEEEEBOOOOOY 5 points")
elif alien_color == "green":
    print("EEEEEBOOOOOY 10 points")
else:
    print("EEEEEBOOOOOY 15 points")

#2)green
alien_color = "green"
if alien_color == "red":
    print("EEEEEBOOOOOY 5 points")
elif alien_color == "green":
    print("EEEEEBOOOOOY 10 points")
else:
    print("EEEEEBOOOOOY 15 points")

#3)yellow
alien_color = "yellow"
if alien_color == "red":
    print("EEEEEBOOOOOY 5 points")
elif alien_color == "green":
    print("EEEEEBOOOOOY 10 points")
else:
    print("EEEEEBOOOOOY 15 points")

# Nom 5.6

#1)Написать цепочку if-elif-else, для определения периода жизни
age = 17
if age < 2:
    print("Ты младенец")
elif age >= 2 and age < 4:
    print("Ты малыш")
elif age >= 4 and age < 13:
    print("Ты ребёнок")
elif age >= 13 and age < 20:
    print("Ты подросток")
elif age >= 20 and age < 65:
    print("Ты взрослый")
elif age >= 65:
    print("Ты пожилой")

# Nom 5.7

#1)Создать список любимых блюд,написать 5 команд if, они должны проверять, входит ли в состав списка
favorite_fruits = ["Shashlik", "pizza", "lulya-kebab"]

if "Shashlik" in favorite_fruits:
    print(f"You really like {favorite_fruits[0]}")

if "pizza" in favorite_fruits:
    print(f"You really like {favorite_fruits[1]}")

if "lulya-kebab" in favorite_fruits:
    print(f"You really like {favorite_fruits[2]}")

favorite_fruits[1] = "Pizza"
if "Pizza" in favorite_fruits[1].title():
    print(f"You really like {favorite_fruits[1]}")

if favorite_fruits[0].lower() == "shashlik" :
    print(f"You really like {favorite_fruits[0]}")

# Nom 5.8

#1)Создать список, пользователю с ником "admin" после "регистрации на сайте" вывести сообщение отличное от других
users = ['David', 'Fred', 'Milana', 'Dabek', 'Admin']
for user in users:
    if user == 'Admin':
        print(f"Hello {users[-1]}, would you like to see a status report?")
    else:
        print(f"\nHello {user}, thank you for login again!")

# Nom 5.9

#1)Если в списке пользователей нет вывести сообщение
users = []
for user in users:
    if user == 'Admin':
        print(f"Hello {users[-1]}, would you like to see a status report?")
    else:
        print(f"\nHello {user}, thank you for login again!")

if users == []:
    print("We need to ind some users")

#'David', 'Fred', 'Milana', 'Dabek', 'Admin'

# Nom 5.10

#1)Проверка уникальности имен пользователей
current_users = ['david', 'fred', 'milana', 'dabek', 'damir']
new_users = ['Disana', 'Fred', 'Murat', 'Dabek', 'Darina']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"You can't use this login  {new_user}\n")
for new_user in new_users:
    if new_user.lower() not in current_users:
        print(f"Welcome, {new_user}")

# Nom 5.11

#1)Вывести порядковые числительные от 1 до 9 цепочкой if-elif-else
for value in range(1,10):
    if value == 1:
        print("1st")
    elif value == 2:
        print("2nd")
    elif value == 3:
        print("3rd")
    else:
        print(f"{value}th")



#Словари

# Nom 6.1

#1)В словаре сохранить информацию о человеке и вывести
people = {
    'first_name': 'Damir',
    'last_name': 'Hejev',
    'age': 13,
    'city': 'Baksan',
    }
print(f"He is {people['first_name']}, his last name is {people['last_name']}, he is {people['age']}")
print(f"{people['first_name']} live in {people['city']}")

# Nom 6.2

#1)Написать любимые числа людей в словаре
people_num = {
    'Damir': 9,
    'Darina': 19,
    'Papa': 13,
    'Dabek': 2,
    'Mama': 7,
    }
people_names = ['damir','darina','papa','dabek','mama']
print(f"{people_names[0].title()}'s favorite number is {people_num['Damir']}")
print(f"{people_names[1].title()}'s favorite number is {people_num['Darina']}")
print(f"{people_names[2].title()}'s favorite number is {people_num['Papa']}")
print(f"{people_names[3].title()}'s favorite number is {people_num['Dabek']}")
print(f"{people_names[4].title()}'s favorite number is {people_num['Mama']}")

# Nom 6.3

#1)Создать словарь в словаре терминов, изученных раннее
slovar = {
    'Переменная': '-это как ярлык, которая содержит ссылку на какое-то значение.',
    'Список': '-набор элементов, следующих в определенном порядке.',
    'Команды if': '-команда, которая позволяет проверить текущие данные программы.',
    'Словари': '-это место хранения пар "ключ значений".',
    'Цикл for': '-это команда, которая перебирает элементы списка.',
    }
print(f"\nПеременная{slovar['Переменная']}")
print(f"\nСписок{slovar['Список']}")
print(f"\nКоманды if{slovar['Команды if']}")
print(f"\nСловари{slovar['Словари']}")
print(f"\nЦикл for{slovar['Цикл for']}")

# Nom 6.4

#1)Автоматизировать, вместо print применить for, добавить 3 "ключ-значения"б вывести 
slovar = {
    'Переменная': '-это как ярлык, которая содержит ссылку на какое-то значение.',
    'Список': '-набор элементов, следующих в определенном порядке.',
    'Команды if': '-команда, которая позволяет проверить текущие данные программы.',
    'Словари': '-это место хранения пар "ключ значений".',
    'Цикл for': '-это команда, которая перебирает элементы списка.',
    }
for key, termin in slovar.items():
    print(f"\n{key} {termin}") 
add_to_slovar = {
    'Метод append()': '-Метод, применяемый для добавления значения в список',
    'or': '-Используется для проверки нескольких условий',
    'and':'-Используется для проверки нескольких условий',
    }
for added_key, added_termin in add_to_slovar.items():
    if added_key not in slovar:
        print(f"\n{added_key} {added_termin}") 

# Nom 6.5

#1)Создать список рек и их местонахождение, с помощью цикла вывести по отдельности и ...
rivers = {
    'nile': 'egypt',
    'baksan': 'baksan',
    'missisipi': 'america',
    }
for river, location in rivers.items():
    print(f"The {river.title()} runs through {location.title()}.")
print('')
for river, location in rivers.items():
    print(river.title())
print('')
for river, location in rivers.items():
    print(location.title())

# Nom 6.6

#1)Использовать программу с любимыми языками людей, применить in и not in
favorite_languages = {
    'damir': 'python',
    'darina': 'c',
    'disana': 'java',
    'dabek': 'js',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print('')
peoples = ['damir', 'dabek', 'disana','papa', 'mama']
for people in peoples:
    if people in favorite_languages.keys():
        print(f'{people.title()}, thank you for vote, you already voted')       
    if people not in favorite_languages.keys():
        print(f'{people.title()}, please vote!')



#Вложения

# Nom 6.7

#1)Добавить в программу 6.1 еще 2 биографии, все словари заключить в список,вывести
people_0 = {
    'first_name': 'damir',
    'last_name': 'hejev',
    'age': 13,
    'city': 'baksan',
    }
people_1 = {
    'first_name': 'darina',
    'last_name': 'hejeva',
    'age': 15,
    'city': 'nalchik',
    }
people_2 = {
    'first_name': 'disana',
    'last_name': 'hejeva',
    'age': 16,
    'city': 'ashhabad'
    }
people = [people_0, people_1, people_2]
for people_info in people:
    full_name = f"{people_info['first_name']} {people_info['last_name']}"    
    print(f"\nName: {full_name.title()} ")
    print(f"Age: {people_info['age']}")   
    print(f"Location: {people_info['city'].title()}")

# Nom 6.8

#1)Также как в предыдущем упражнении, но с дом.животными
bobik = {'poroda': 'русский спаниель', 'hozyain': 'дамир','nick': 'bobik'}
reksik = {'poroda': 'помесь таксы', 'hozyain': 'дамир', 'nick': 'reksik'}
pets = [bobik, reksik]
for pet_info in pets:
    print(f"\nЭто {pet_info['nick'].title()} , он {pet_info['poroda']}")
    print(f"Имя хозяина: {pet_info['hozyain']}")

# Nom 6.9

#1)Создать словарь, ключи-люди, значения-любимые места, могут быть 2 ллюбимыхх места
favorite_places = {
    'damir': ['london', 'elbrus'],
    'darina': ['elbrus'],
    'disana': ['parish', 'kreml'],
    }
for name,places in favorite_places.items():
    name = name.title()
    if len(places) == 1:
        print(f"\n{name}'s favorite place is:")
    if len(places) == 2:
        print(f"\n{name}'s favorite places are:")
    for place in places:
        print(place.title())

# Nom 6.10

#1)Усовершенствовать программу из упражнения 6.2, добавить несколько любимых чисел
people_num = {
    'damir': [9, 2, 3],
    'darina': [19, 54, 78],
    'papa': [13, 11],
    'dabek': [2, 6],
    'mama': [7],
    }
favorite_numbers = people_num.values()
for people_name,favorite_numbers in people_num.items():
    if len(favorite_numbers) == 1:
        print(f"{people_name.title()}'s favorite number is {favorite_numbers}")
    else:
        print(f"{people_name.title()}'s favorite numbers are {favorite_numbers}")

# Nom 6.11

#1)В словаре с именем cities, вводим информацию о 3 странах, выводим
cities = {
    'london': {
        'name': 'london',
        'country': 'england',
        'population': 9_000_000,
        'fact': 'this is capital of England',
        },
    'baksan': {
        'name': 'baksan',
        'country': 'russia',
        'population': 38_000,
        'fact': 'the best country',
        },
    'parish': {
        'name': 'parish',
        'country': 'french',
        'population': 2_140_000,
        'fact': 'no facts',
        },
    }
for city_name,city_info in cities.items():
    print("\nName:")
    print(f"\t{city_info['name'].title()}")
    print("His country:")
    print(f"\t{city_info['country'].title()}")
    print('Population there:')
    print(f"\t{city_info['population']}")
    print('Facts about this city:')
    print(f"\t{city_info['fact'].title()}")




#input() и циклы while

# Nom 7.1

#1)Спросить у пользователя, какую машину он хочет.Выведите сообщение с ответом
car = input('Какую машину вы хотите: ')
print(f'{car} очень хорошая машина')

# Nom 7.2

#1)Спросить у пользователя о количестве мест, которые он хочет заказать если > 8, сказать, что мест нет
table = input('Сколько ест вы хотите заказать?: ')
table = int(table)
if table > 8:
    print('Пожалуйста подождите.')
else:
    print('Проходите.У нас есть места')

# Nom 7.3

#1)Запросить у пользователя число, вывести, если оно кратно 10-ти
number = input('Введите число, чтобы узнать, кратно ли оно 10-и: ')
number = int(number)
if number % 10 == 0:
    print(f'\nЧисло {number} кратно 10-ти')
else:
    print(f'\nЧисло {number} не кратно 10-ти')

# Nom 7.4

#1)Написать цикл для добавления наполнения для пиццы, добавить возможноть выйти, при ключевом слове
prompt = "\nPlease print your toppings"
prompt += "\nEnter 'quit' if you want exit."
topping = ''
toppings = []
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(topping)
        toppings.append(topping)
        print(toppings)

# Nom 7.5

#1)Установить несколько вариантов цен на билет в зависимости от возраста
prompt = "\nPlease write your age"
prompt += "\nEnter 'quit' if you want to exit"
message = ''
while message != 'quit':
    message = int(input(f"\n{prompt} "))
    if message < 3:
        print("\nPrice: 0RUB")
    elif message >= 3 and message < 12:
        print("\nPrice: 100RUB")
    elif message >= 12:
        print("\nPrice: 200RUB")

# Nom 7.6

#1)Применить к программам из упражнений 7.4 и 7.5 проверку условия и команду break
time = 0
active = True
prompt = "\nPlease write your age"
prompt += "\nEnter 'quit' if you want to exit"
message = ''
while active:
    message = int(input(f"\n{prompt} "))
    time += 1
    if message < 3:
        print("\nPrice: 0RUB")
    elif message >= 3 and message < 12:
        print("\nPrice: 100RUB")
    elif message >= 12:
        print("\nPrice: 200RUB")
    elif message == 'quit':
        break
    print(time)
    if time == 10:
        active = False

#2)Из упражнения 7.4
limit = 10
active = True
prompt = "\nPlease print your toppings"
prompt += "\nEnter 'quit' if you want exit."
topping = ''
toppings = []
while active:
    topping = input(prompt)
    if topping != 'quit':
        print(topping)
        toppings.append(topping)
        print(toppings)
    if topping == 'quit':
        break
    limit -= 1
    if limit == 0:
        active = False
    print(limit)

# Nom 7.7

#1)Написать бесконечный цикл
x = 1
while x <= 5:
    print(x)

# Nom 7.8

#1)Создать список с элементами, переместить их в другой, вывести все
sandwich_orders = ['burger', 'pizza', 'sandwich', 'fri']
finished_sandwiches = []
while sandwich_orders:
    finish_sandwich = sandwich_orders.pop()
    print(f"Ваш(а) {finish_sandwich} готов(а) ")
    finished_sandwiches.append(finish_sandwich)
print("Мы закончили, вот что мы сделали:")
print(f"\n{finished_sandwiches}")

# Nom 7.9

#1)В список из упр. 7.8 добавить 3 одтнаковх значения,удалить их, вывести
sandwich_orders = ['burger', 'pastrami', 'pizza', 'pastrami', 'sandwich', 'fri', 'pastrami']
finished_sandwiches = []
print("Извините 'pastrami' больще нет")
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    finish_sandwich = sandwich_orders.pop()
    print(f"Ваш(а) {finish_sandwich} готов(а) ")
    finished_sandwiches.append(finish_sandwich)
print("Мы закончили, вот что мы сделали:")
print(f"\n{finished_sandwiches}")

# Nom 7.10

#1)Провести опрос и вывести результаты
active = True
responses = {}
while active:
    name = input("\nПожалуйста введите имя:")
    response = input("Какую страну вы хотите посетить: ")
    responses[name] = response

    repeat = input("\n\tВы хотите продолжить?(да/нет) ")
    if repeat == 'нет':
        active = False
        print("\n---Результаты---")
        for name,response in responses.items():
            print(f"{name.title()} хочет пойти в {response.title()}")





#Функции

# Nom 8.1

#1)Написать функцию, вызвать функцию
def display_message():
    print("Запись простая")
display_message()

# Nom 8.2

#1)Написать функцию, добавить параметр и аргумент
def favorite_book(title):
    print(f"My favorite book is '{title.title()}'")
favorite_book("Robin good")

# Nom 8.3

#1)Написать функцию, ввести параметры и аргументы
#(позиционные и именованные), вывести
def make_shirt(size, text):
    print(f"This is {text}, size = {size}")
make_shirt('XXL', 'very good shirt')
make_shirt(size = 'XL', text = 'very bad shirt')

# Nom 8.4

#1)Изменить программу из упр. 8.3, добавить параметры
#по умолчанию, изменить, вывести
def make_shirt(size = 'L', text = '"I love Python"'):
    print(f"Text - {text}, size - {size}")
make_shirt()
make_shirt('2XL', '"I love C"')
make_shirt(size = '3XL', text = '"I love java"')

# Nom 8.5

#1)Создать функцию с параметром по умолчанию, несколько раз изменить
def describe_city(city_name, country_name = 'Russia'):
    print(f"{city_name.title()} is in {country_name.title()}")
describe_city('moscow')
describe_city(city_name = 'new york')
describe_city('london', 'UK')

# Nom 8.6

#1)Создать функцию, сохранить аргументы в словаре, вывести словарь
def build_city_country(city_name, country_name):
    city_country = {'city' : city_name, 'country' : country_name,}
    print(city_country)
    return city_country
build_city_country('london', 'england')
build_city_country('baksan', 'RUSSIA')

# Nom 8.7

#1)Создать альбом заполнить три раза, использовать необяз. аргументы
def build_make_album(name_singer, name_albom, sum_songs = None):
    singers = {}
    if sum_songs:
        singers['sum_songs'] = sum_songs
        singers['name_singer'] = name_singer
        singers['name_albom'] = name_albom
    else:
        singers['name_singer'] = name_singer
        singers['name_albom'] = name_albom
    return singers
print(build_make_album('damir', 'damirkrasava', 66))
print(build_make_album('darina', 'darinakrasava', 77))
print(build_make_album('disana', 'disanakrasava', 11))

# Nom 8.8

#1)Изменить программу 8.7, добавить цикл while, input, break
def build_make_album(name_singer, name_albom, sum_songs = None):
    singers = {}
    if sum_songs:
        singers['sum_songs'] = sum_songs
        singers['name_singer'] = name_singer
        singers['name_albom'] = name_albom
    else:
        singers['name_singer'] = name_singer
        singers['name_albom'] = name_albom
    return singers
while True:
    print("\nPlease indicate information:")
    print("Press 'q' to quit")
    n_singer = input("Name singer: ")
    if n_singer == 'q':
        break
    n_albom = input("Name albom: ")
    if n_albom == 'q':
        break
    s_songs = input("Sum songs: ")
    if s_songs == 'q':
        break
    musician = build_make_album(n_singer, n_albom, s_songs)
    print(musician)

# Nom 8.9

#1)Создать функцию, перебрать список с помощью for
def show_messages(texts):
    for text in texts:
        print(text)
texts = ['Нет террору', 'Дабек не молодец', 'Дамир молодец']
show_messages(texts)

# Nom 8.10

#1)Внести изменения в программу из упр. 8.9
def great_text(unverified_spisok_texts , verified_spisok_texts):
    while unverified_spisok_texts:
        current_spisok_texts = unverified_spisok_texts.pop()
        print('Generation texts: ')
        print(f"\t{current_spisok_texts}")
        verified_spisok_texts.append(current_spisok_texts)
def show_completed_texts(verified_spisok_texts):
    print("\nPrinted models: ")
    for verified_spisok_text in verified_spisok_texts:
        print(verified_spisok_text)
unverified_spisok_texts = ['Нет террору', 'Дамир молодец', 'Дабек не молодец']
verified_spisok_texts = []
great_text(unverified_spisok_texts, verified_spisok_texts)
show_completed_texts(verified_spisok_texts)

# Nom 8.11

#1)В программе из упр. 8.10 копировать список до изменений
def send_messages(unverified_spisok_texts):
    print("\nUnverified spisok texts before:")
    for unverified_spisok_text in unverified_spisok_texts:
        print(unverified_spisok_text)
def great_text(unverified_spisok_texts , verified_spisok_texts):
    while unverified_spisok_texts:
        current_spisok_texts = unverified_spisok_texts.pop()
        print('\nGeneration texts: ')
        print(f"\t{current_spisok_texts}")
        verified_spisok_texts.append(current_spisok_texts)
def show_completed_texts(verified_spisok_texts, unverified_spisok_texts):
    print("\nPrinted models: ")
    for verified_spisok_text in verified_spisok_texts:
        print(verified_spisok_text)
    print("\nUnverified spisok texts after:")
    for unverified_spisok_text in unverified_spisok_texts:
        print(unverified_spisok_text)
def send_messages(unverified_spisok_texts):
    print("\nUnverified spisok texts before:")
    for unverified_spisok_text in unverified_spisok_texts:
        print(unverified_spisok_text)
unverified_spisok_texts = ['Нет террору', 'Дамир молодец', 'Дабек не молодец']
verified_spisok_texts = []
send_messages(unverified_spisok_texts[:])
great_text(unverified_spisok_texts, verified_spisok_texts)
show_completed_texts(verified_spisok_texts, unverified_spisok_texts)

# Nom 8.12

#1)Создать функцию, дать один параметр для n-ного кол-ва значений, вывести
def make_sandwitch(*components):
    print('\nComponents: ')
    for component in components:
        print(component)
make_sandwitch("грибы")
make_sandwitch('грибы', 'листья')
make_sandwitch('грибы', 'листья', 'колбаса')

# Nom 8.13

#1)В программе , сделанной раннее, применить свою информацию.
def build_profile(first , last , **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('damir', 'hejev',
                             location = 'baksan',
                             profechiom = 'student')
print(user_profile)

# Nom 8.14

#1)Написать функцию, задать параметры, пара-тр произвольного кол-во аргум.
def build_auto(marka, name, **car_info):
    car_info["mark"] = marka
    car_info["name"] = name
    return car_info
car_profile = build_auto('subaru', 'outback',
                         color = 'blue', tow_package = True)
print(car_profile)

# Nom 8.15

#1)Из модуля вызвать функцию(модуль)
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
#2)(Вызов модуля и функции)
from printing_functions import print_models
from printing_functions import show_completed_models

unprinted_designs = ['dabek', 'robot', 'cube']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)








#Классы

# Nom 9.1

#Создать класс, метод __init__ должен содержать два атрибута, создать экземпляр
class Restaurant():
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant '{self.restaurant_name} is good.")
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} has {self.cuisine_type} type.")
restaurant1 = Restaurant("In_time", "sushi")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

# Nom 9.2

#Создать ещё два экземпляра
class Restaurant():
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"\nRestaurant '{self.restaurant_name} is good.")
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} has {self.cuisine_type} type.")
#Первый ресторан
restaurant1 = Restaurant("In_time", "sushi")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

#Второй ресторан
restaurant2 = Restaurant("Art", "shashlik")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

#Третий ресторан
restaurant3 = Restaurant("Best", "shaverma")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

# Nom 9.3

#Создать класс. Применить метод __init__. Создать несколько экземпляров
class User():
    def __init__(self , first_name , last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"\nUser's describe: {self.last_name.title()}"
            f"{self.first_name.title()} not nervous people")
    def greet_user(self):
        print(f"User's greet: Hi, my name is {self.first_name}")

#Первый пользователь        
user1 = User("Damir", "Hejev")
user1.describe_user()
user1.greet_user()

#Второй пользователь
user2 = User('Darina', "Hejeva")
user2.describe_user()
user2.greet_user()

#Третий пользователь 
user3 = User("Disana", "Hejeva")
user3.describe_user()
user3.greet_user()











































































































































































