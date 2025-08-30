class User:
	def __init__(self, name: str, age: int, gender: str) -> None:
		self.__name = name
		self.__age = age
		self.__gender = gender

	def show_details(self) -> str:
		print(f"Personal details")
		print("")
		print(f"Name : {self.__name}")
		print(f"Age : {self.__age}")
		print(f"Gender : {self.__gender}")


class Bank(User):
	def __init__(self, name: str, age: int, gender: str) -> None:
		super().__init__(name, age, gender)
		self.__balance = 0

	def view_balance(self) -> str:
		print(f"Your account balance is ${self.__balance}")

	def deposit(self, balance: float) -> str:
		if balance > 0:
			self.__balance += balance
			print(f"Successfully deposit ${balance}")
		else:
			print(f" ${balance} is not validate on deposit")

	def withdraw(self, balance: float) -> str:
		if balance <= self.__balance and balance > 0:
			self.__balance -= balance
			print(f"Successfully withdraw ${balance}")
		else:
			print(f" ${balance} is not validate on withdraw")



