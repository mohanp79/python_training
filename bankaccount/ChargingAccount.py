class ChargingAccount(BankAccount):
    def __init__(self, initialAmount):
        BankAccount.__init__(self, initialAmount)
        self.fee = 3
        
    def withdraw(self, amount):
        BankAccount.withdraw(self, amount+self.fee)
