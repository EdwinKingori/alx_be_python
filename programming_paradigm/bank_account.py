# class definition
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"You deposited ${amount}")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrawn amount is: ${amount}")
                print(f"Your balance is {self.__account_balance}")
                return True
            else:
                print("insufficient funds to conduct this withdrawal")
                return False
        else:
            print("Insufficient funds to withdraw.")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.__account_balance:.2f}")


account = BankAccount(2000)
print(account.display_balance())

account.deposit(500)
print(account.display_balance())

success_withdraw = account.withdraw(70)
print(success_withdraw)
account.display_balance()

failure = account.withdraw(200)
print(failure)
account.display_balance()
