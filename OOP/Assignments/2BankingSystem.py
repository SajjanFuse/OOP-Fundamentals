"""
Build a Python class to represent a simple banking system. Create a class for a BankAccount, and another for Customer. The BankAccount class should have a constructor to initialize the account details (account number, balance, account type). The Customer class should have a constructor to set the customer's details (name, age, address) and create a BankAccount object for each customer. Implement a destructor for both classes to display a message when objects are destroyed.

"""
import logging 

logging.basicConfig(filename='banking_system.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BankAccount:
    def __init__(self, ac_no, acc_type, balance):
        self.__ac_no = ac_no 
        self.__acc_type = acc_type 
        self.__balance = int(balance)
        logging.info(f'Bank Account created of {self.__ac_no}')

    def get_account_number(self):
        return self.__ac_no
    
    def deposit(self, amount):
        logging.info(f'Old balance is {self.__balance} of {self.__ac_no}')
        logging.info(f'Amount of{amount} deposited to {self.__ac_no}')
        self.__balance +=amount 
        logging.info(f'New balance is {self.__balance} deposited to {self.__ac_no}')

    def withdraw(self, amount):
        if(self.__balance-amount <0):
            logging.warning(f'{amount} is not present in {self.__ac_no}')
            return 
        self.__balance -= amount 
        logging.info(f'Amount of{amount} withdrawn from {self.__ac_no}')
        

    def __del__(self):
        
        logging.info(f'Bank Account destructed of {self.__ac_no}')


class Customer:
    def __init__(self, name, age, address):
        self._name = name 
        self._age = age 
        self._address = address
        self._bank_account = None 

    def create_account(self, account_number, balance = 0, acc_type = "Savings"):
        self._bank_account = BankAccount(ac_no=account_number, acc_type=acc_type, balance=balance)

    def deposit(self, amount):
        if self._bank_account:
            self._bank_account.deposit(amount)
        else:
            print("No bank account available.")

    def withdraw(self, amount):
        if self._bank_account:
            self._bank_account.withdraw(amount)
        else:
            print("No bank account available.")

    def get_balance(self):
        if self._bank_account:
            return self._bank_account.get_balance()
        else:
            print("No bank account available.")

    def __del__(self):
        logging.info(f'Customer: {self._name} is deleted!')

try:
    # Create customer and bank account
    customer1 = Customer("Ram", 30, "Baneshwor")
    customer1.create_account("123456", 1000)

    # Perform transactions
    customer1.deposit(500)
    customer1.withdraw(200)

    customer1.withdraw(2500)
    # Delete customer (destructor will be called)
    del customer1


except Exception as e:
    print("An error occurred:", e)