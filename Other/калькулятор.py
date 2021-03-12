active = True
print("Hello")
while active:
    quit = input("\n\tPrint 'q' for quit")
    if quit == 'q':
        break
    class calculations():
        def sum(f_number, l_number):
            c = a + b
            print(f"\tРезультат: {c}")

        def minus(f_number, l_number):
            c = a - b
            print(f"\tРезультат: {c}")

        def multiplication(f_number, l_number):
            c = a * b
            print(f"\tРезультат: {c}")

        def division(f_number, l_number):
            c = a / b
            print(f"\tРезультат: {c}")

        def degree(f_number, l_number):
            c = a ** b
            print(f"\tРезультат: {c}")
            
        def remainder_of_the_division(f_number, l_number):
            c = a % b
            print(f"\tРезультат: {c}")
            
        def integer_division(f_number, l_number):
            c = a // b
            print(f"\tРезультат: {c}")

"""Сбор данных для вычисления"""
    a = float(input("\nВведите число: "))
    what = input("Знак: ")
    b = float(input("Введите число: "))
        
    """if- ы для вызова функций вычисления"""

    if what == "+":
        calculations.sum(a, b)
    if what == "-":
        calculations.minus(a, b)
    if what == "*":
        calculations.multiplication(a, b)
    if what == "/":
        calculations.division(a, b)
    if what == "^":
        calculations.degree(a, b)
    if what == "%":
        calculations.remainder_of_the_division(a, b)
    if what == "//":
        calculations.integer_division(a, b)



