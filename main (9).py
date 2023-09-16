#main.py#2.1 implement a class called Bank account that represents a Bank account.The class should have private attributes for a account  number, account holder name, and account balance. include methods to deposit money, with draw money, and display the account balance ensure that the account balance cannot be accessed directly from outside the class. write a program to create an instance of the bank account class and test the deposit and withdrawal functionally.
class BankAccount:
  def_init_(self,account_number,account_holder_name,initial_balance=0.0):
    self.account_number=account_number
     self._account_holder_name=account _holder_name
   self._account_balance=initial_balance  
 def deposit (self,amount):
  if amount >0:
    self._account += amount 
  print(f"Deposit${amount:.2f}into account{self._account_number}")
else:
print(invalid deposit amount.please deposit a positive amount.")
def withdraw(self.amount):
  if amount >0:
    if self._amount_balance>=amount:
    self_account_balance-= amount
    print(f"withdraw ${amount:.3f} from account{self.account_number}")
    else:
    print ("insufficient balance.cannot withdraw.")
else:
print("invalid withdrawal amount.please withdraw a positive amount.")
def display_balance(Self):
print(f"Account{self.-account_ number balance:${salf._account_balance:.2f}")
# Testing the Bank account class
# create a Bank account instance
account 1 Bank = account ("123456","Jhohn Doe",1000.0)

# Deposit money 
  account 1.deposit(500.0)
# withdraw money 
  account 1.withdraw(200.0)
# Display balance 
  account 1.display_balance()
