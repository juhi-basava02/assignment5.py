# handling a bank account

class Account:
    def _init_(self, balance=0):
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def _init_(self, balance=0, interest_rate=0.05):
        super()._init_(balance)
        self.interest_rate = interest_rate

    def interestAmount(self):
        return self.balance * self.interest_rate

def main():
    account = Account(1000)
    account.deposit(500)
    print(account.getBalance())

    savings_account = SavingsAccount(1000, 0.05)
    print(savings_account.interestAmount())

