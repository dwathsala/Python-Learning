class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    #method to deposit money
    def deposit(self, amount):
        self.balance += amount
        return "Successfull - Deposite"
    
    #method to withdraw money
    def withdraw(self, amount):
        self.balance -= amount
        return "Successfull - Withdraw"
    
bal = BankAccount("123456789", "John Doe", 1000) #bank account open with initial balance of 1000
print(bal.balance)  # Output: 1000
print(bal.deposit(500))  # Output: Successfull - Deposite
print(bal.balance)  # Output: 1500
print(bal.owner)  # Output: John Doe
print(bal.withdraw(200))  # Output: Successfull - Withdraw
print(bal.balance)  # Output: 1300