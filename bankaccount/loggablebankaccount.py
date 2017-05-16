# File: loggablebankaccount.py
#
# Extend Bank account classes to work with logger module.
###############################

import bankaccount_general, logger

class LoggableBankAccount(bankaccount_general.BankAccount, logger.Logger):
    def activity(self):
       return ("Account balance = ", self.checkBalance())

class LoggableInterestAccount(bankaccount_general.InterestAccount,
                              logger.Logger):
    def activity(self):
       return ("Account balance = ", self.checkBalance())

class LoggableChargingAccount(bankaccount_general.ChargingAccount,
                              logger.Logger):
    def activity(self):
       return ("Account balance = ", self.checkBalance())
