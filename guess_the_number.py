import random
from random import randint
active = True
while active:
	#Задаются числа
	def assignment_of_values():
		a = float(random.randint(1,14))
		b = float(random.randint(1,14))
		if b > a:
			assignment_of_values()
		else:
			calculations(a , b)
	#Вычисления
	def calculations(*values):
		c = a / b
		interview()
	#Ввод данных пользователя
	def interview():
		text = float(input("Результат: "))
		result()
	#Результат
	def result()
		if text == c:
			print("Правильно")
			continue
		else:
			interview()


