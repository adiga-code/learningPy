what = input(' "+" или "-" или "/" или "*" ? ')

a = float( input("Первое число: " ) )
b = float( input("Второе число: " ) )
 
if what == "+" :
    c = a + b
    print("Результат: " + str(c) )
elif what == "-" :
    c = a - b
    print("Результат: " + str(c) )
if what == "/" :
    c = a / b
    print("Результат: " + str(c) )
elif what == "*":
    c = a * b
    print("Результат: " + str(c) )
else:
    print("Неверная операция! " )