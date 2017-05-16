class InterestAccount(BankAccount):
   def deposit(self, amount):
       BankAccount.deposit(self,amount)
       self.balance = self.balance * 1.03
