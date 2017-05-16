class BalanceError(Exception): 
      value = "Sorry you only have $%6.2f in your account"

class BankAccount:
    def __init__(self, initialAmount):
       self.balance = initialAmount
       print ("Account created with balance: ", self.balance)

    def deposit(self, amount):
       self.balance = self.balance + amount

    def withdraw(self, amount):
       if self.balance >= amount:
          self.balance = self.balance - amount
       else:
          raise (BalanceError, BalanceError.value % self.balance)

    def checkBalance(self):
       return self.balance
       
    def transfer(self, amount, account):
       try: 
          self.withdraw(amount)
          account.deposit(amount)
       except BalanceError:
          print (BalanceError.value)


class ChargingAccount(BankAccount):
    def __init__(self, initialAmount):
        BankAccount.__init__(self, initialAmount)
        self.fee = 3
        
    def withdraw(self, amount):
        BankAccount.withdraw(self, amount+self.fee)

class InterestAccount(BankAccount):
   def deposit(self, amount):
       BankAccount.deposit(self,amount)
       self.balance = self.balance * 1.03
