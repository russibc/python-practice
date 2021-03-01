from bank_account import BankAccount

account = BankAccount()
account.set_accountNumber('123-4')
account.deposit(50.0)
account.set_limit(1500.0)
account.set_owner('Ada Lovelace')

print(f'Balance before deposit: {account.balance}')

print(f'Depositing 100 in {account.get_owner()} account...')
account.deposit(100)

print(f'Balance now: {account.displayBalance()}')

account.withdraw(150.0)

print(f'Balance now: {account.displayBalance()}')

account.withdraw(50.0)
