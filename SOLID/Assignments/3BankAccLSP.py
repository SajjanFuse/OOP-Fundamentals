"""
[Liskov Substitution Principle (LSP)] Download the python file from this link. In this file, there is an implementation of a banking system for account handling. There is a savings account and a checking account class. The checking account inherits the savings account as both have the same functionality and the checking account allows overdrafts (allow processing transactions even if there is not sufficient balance). Redesign this program to follow the  Liskov Substitution Principle (LSP) principle which represents that “objects should be replaceable by their subtypes without altering how the program works”. 
"""
# object of child class replaces objet of a parent class, (while calling a method) and does not break the application 
# all the base class methods must be applicable to the derived classes also 

"""
Solution: 
    - correct inheritance hierarchy! 
    - Vehicle class 
        - method startEngine() 

    - Car(Vehicle) 
        - method startEngine(), overridden but works 
    - Cycle(Vehicle)
        - method startEngine() is obsolete, doesn't work at all
    This breaks the LSP.

    Solution is: 
        - differentitating classes of transportation as
            - with engines
            - without engines! 

"""
# changing the inheritance hierarchy in this example as well
class Account():
    def __init__(self, balance) -> None:
        self.balance = balance

    def withdraw(self, amount):
        # Savings account does not allow overdrafts
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

        else:
            print("Insufficient funds!")

class SavingsAccount(Account):
    pass 

class CheckingAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Checking account allows overdrafts but with a limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account):
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)

if __name__ == "__main__":
    # Creating instances of SavingsAccount and CheckingAccount
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    # Performing actions on both accounts
    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)