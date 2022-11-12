#Bank Account Manager - Create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount and BusinessAccount. 
# Manage credits and debits from these accounts through an ATM style program.

# Handling a Bank Account

class Bank_Account:
	def __init__(self):
		self.balance=0
        
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:")

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:")
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)

class Savings_Account(Bank_Account):
    def _init_(self,balance,amount):
        super()._init_(balance)
        self.amount = amount
    def display(self,amount):
		   if self.balance==amount:
	            print("\n Net Available Balance=",self.balance)

# Driver code

# creating an object of class
self = Bank_Account()


self.deposit()
self.withdraw()
self.display()  

self = Savings_Account (Bank_Account)
self.display()
