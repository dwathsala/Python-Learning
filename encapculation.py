class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.__ccount_number = account_number
        self.__owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        return "Successfull - Deposite"
    
    def __withdraw(self, amount): 
        self.__balance -= amount
        return "Successfull - Withdraw"
    
    def get_balance(self):
        return self.__balance
    
    def get_account_info(self):
        return f"Account Number: {self.__ccount_number}, Owner: {self.__owner}, Balance: {self.__balance}"
    
    def set_balance(self, amount):
        self.__balance = amount # this method can be use to change the balance but not recommended, because it breaks the encapculation principals...

    def set_owner_name(self, new_owner_name):
        self.__owner = new_owner_name # this method can be use to change the owner but not recommended, because it breaks the encapculation principals...

acc1 = BankAccount("123456789", "John Doe", 1000) 
print(acc1.deposit(500))  # Output: Successfull - Deposite

print(acc1.get_balance())  # Output: 1500
print(acc1.get_account_info())  # Output: Account Number: 123456789, Owner: John Doe, Balance: 1500

# Get new owner name from user
new_name = input("Enter new owner name: ")

# Update owner name
acc1.set_owner_name(new_name)

# Print updated details
print(acc1.get_account_info())



'''acc1.deposit(500)
print(acc1.balance)'''