class BankAccount:
    def __init__(self,owner,balance = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        return self.balance
    
    def withdraw(self,withdrawal_amount):
        self.balance -= withdrawal_amount
        return self.balance
    
acct = BankAccount("Darcy")
acct.deposit(10)
acct.withdraw(3)

print(acct.balance)