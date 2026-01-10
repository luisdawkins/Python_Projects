# Write code below 💖
class BankAccount():
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance ):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
  
  def withdraw(self, amount):
    self.balance -= amount
  
  def display_balance(self):
    print(f"Your balance is {self.balance}. Is that all {self.first_name}?")
  
Me = BankAccount("John", "Smith", 1001, "beginner", 1234, 400.00)

Me.deposit(96)
Me.withdraw(25)
Me.display_balance()
