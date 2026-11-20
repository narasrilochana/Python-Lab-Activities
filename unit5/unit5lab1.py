
class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited: $%.2f" % amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print("Withdrew: $%.2f" % amount)

    def check_balance(self):
        print("Account Holder: %s | Current Balance: $%.2f" %
              (self.account_holder, self.balance))


# Example Usage
account = BankAccount("Alex", 1000.0)

account.check_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.check_balance()
