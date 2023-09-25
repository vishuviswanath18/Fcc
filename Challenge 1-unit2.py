class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited Rs {amount}. New balance: Rs {self._account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew Rs {amount}. New balance: Rs {self._account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self._account_holder_name}: Rs {self._account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    my_account = BankAccount("123456789", "John", 1000.0)

    # Test deposit and withdrawal
    my_account.display_balance()
    my_account.deposit(500.0)
    my_account.withdraw(200.0)
    my_account.display_balance()
