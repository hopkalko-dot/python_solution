class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._bal = balance
        self.hist = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self._bal += amount
        self.hist.append(('dep', amount))

    def withdraw(self, amount):
        if amount <= 0 or amount > self._bal:
            raise ValueError
        self._bal -= amount
        self.hist.append(('wd', amount))

    def get_balance(self):
        return self._bal

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self._bal - amount < 100:
            raise ValueError
        super().withdraw(amount)

class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, limit=1000):
        super().__init__(owner, balance)
        self.limit = limit

    def withdraw(self, amount):
        if self._bal - amount < -self.limit:
            raise ValueError
        self._bal -= amount
        self.hist.append(('wd', amount))

a = BankAccount('A', 100)
a.deposit(50)
print(a.get_balance())
