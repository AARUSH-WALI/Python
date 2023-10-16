class ATM:
    def __init__(self, balance):
        self.balance = balance
    
    def check_balance(self):
        return self.balance
    
    def withdraw(self, amouclass ):
        def __init__(self, balance):
            self.balance = balance
            def check_balance(self):
                return self.balance
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance"
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

# Example usage
atm = ATM(1000)

print("Your balance is:", atm.check_balance())

amount = int(input("Enter amount to withdraw: "))
print("You withdrew:", atm.withdraw(amount))
print("Your balance is:", atm.check_balance())

amount = int(input("Enter amount to deposit: "))
print("Your balance is:", atm.deposit(amount))
if self.balance >= amount:
    self.balance -= amount
    return amount
else:
    return "Insufficient balance"
def deposit(self, amount):
    self.balance += amount
    return self.balance

# Example usage
atm = ATM(1000)

print("Your balance is:", atm.check_balance())

amount = int(input("Enter amount to withdraw: "))
print("You withdrew:", atm.withdraw(amount))
print("Your balance is:", atm.check_balance())

amount = int(input("Enter amount to deposit: "))
print("Your balance is:", atm.deposit(amount))
