# implement a banking account

class Account:

    def _init_(self, title, balance):
        self.title = title
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            return False

        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount < 0:
            return False

        if amount > self.balance:
            return False

        self.balance -= amount
        return True

class SavingsAccount(Account):

    def _init_(self, title, balance, interest_rate):
        super()._init_(title, balance)
        self.interest_rate = interest_rate

    def accumulate_interest(self):
        self.balance += self.balance * self.interest_rate

