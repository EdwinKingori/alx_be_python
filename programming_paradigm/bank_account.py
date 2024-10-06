# class definition
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew: ${amount:.1f}")
                # print(f"Withdrawn amount is: ${amount:.2f}")
                # print(f"Your balance is {self.__account_balance:.2f}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")
