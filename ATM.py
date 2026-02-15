# MINI PROJECT: ATM MANAGEMENT SYSTEM USING OOPS
# ---------------------------------------------
# Demonstrates:
# Class, Object, Encapsulation, Inheritance,
# Abstraction, Polymorphism, Instance/Class/Static Methods

from abc import ABC, abstractmethod   # For abstraction


# ================================
# PART 1: Abstract Class
# ================================
class BankAccount(ABC):

    @abstractmethod
    def transaction(self):
        pass   # No logic here (abstraction)


# ================================
# PART 2: Base Class (Encapsulation)
# ================================
class Account(BankAccount):

    bank_name = "ABC Bank"   # Class variable

    def __init__(self, name, acc_no, balance):
        self.name = name              # Public variable
        self._acc_no = acc_no          # Protected variable
        self.__balance = balance      # Private variable

    # Getter method for private balance
    def get_balance(self):
        return self.__balance

    # Setter method for private balance
    def set_balance(self, amount):
        self.__balance = amount

    # Parent method (will be overridden)
    def transaction(self):
        print("Processing bank transaction...")


# ================================
# PART 3: Child Class (Inheritance)
# ================================
class ATM(Account):

    # Class Method
    @classmethod
    def display_bank_name(cls):
        print(f"\nWELCOME TO {cls.bank_name} ATM")

    # Static Method
    @staticmethod
    def validate_amount(amount):
        return amount > 0

    # Method Overriding (Polymorphism)
    def transaction(self):
        print("ATM transaction started...\n")

    # Instance Method
    def check_balance(self):
        print(f"Current Balance: ₹{self.get_balance()}")

    # Instance Method
    def deposit(self, amount):
        if self.validate_amount(amount):
            new_balance = self.get_balance() + amount
            self.set_balance(new_balance)
            print("Deposit successful!")
            print(f"Updated Balance: ₹{new_balance}")
        else:
            print("Invalid deposit amount!")
            # Instance Method
    def withdraw(self, amount):
        if not self.validate_amount(amount):
            print("Invalid withdrawal amount!")
        elif amount > self.get_balance():
            print("Insufficient balance!")
        else:
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print("Withdrawal successful!")
            print(f"Remaining Balance: ₹{new_balance}")

    # Instance Method
    def account_details(self):
        print("\nACCOUNT DETAILS")
        print("----------------")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self._acc_no}")
        print(f"Balance: ₹{self.get_balance()}")


# ================================
# PART 4: Menu-Driven Program
# ================================

# Creating ATM object
user = ATM("VEERA", 769834, 2000)

ATM.display_bank_name()
user.transaction()

while True:
    print("\n-----------------------------")
    print("ATM MENU")
    print("1. Check the Balance")
    print("2. Deposit the Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")
    print("-----------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        user.check_balance()

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        user.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        user.withdraw(amount)

    elif choice == "4":
        user.account_details()

    elif choice == "5":
        print("\nThank you for using ABC Bank ATM. Visit again!")
        break

    else:
        print("Invalid choice! Please try again.")
