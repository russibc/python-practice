class BankAccount:

    def __init__(self):
        self.balance = 0

    def get_accountNumber(self):
        return self.accountNumber

    def get_owner(self):
        return self.owner

    def get_limit(self):
        return self.limit

    def set_accountNumber(self, accountNumber):
        self.accountNumber = accountNumber

    def set_owner(self, owner):
        self.owner = owner

    def set_limit(self, limit):
        if(limit <= 0):
            print('Your limit must at least 50')
        else:
            self.limit = limit

    def deposit(self, amount):
        self.balance += amount

    def displayBalance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'You withdrew: {amount}')
        else:
            print(f'You cannot withdraw')
