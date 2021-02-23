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








































