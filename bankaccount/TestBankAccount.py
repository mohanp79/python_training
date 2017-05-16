from bankaccount import *
    
# First a standard BankAccount
    a = BankAccount(500)
    b = BankAccount(200)
    a.withdraw(100)
# a.withdraw(1000)
    a.transfer(100,b)
    print ("A = ", a.checkBalance())
    print ("B = ", b.checkBalance())
    
    
# Now an InterestAccount
    c = InterestAccount(1000)
    c.deposit(100)
    print ("C = ", c.checkBalance())
    
    
# Then a ChargingAccount
    d = ChargingAccount(300)
    d.deposit(200)
    print ("D = ", d.checkBalance())
    d.withdraw(50)
    print ("D = ", d.checkBalance())
    d.transfer(100,a)
    print ("A = ", a.checkBalance())
    print ("D = ", d.checkBalance())
    
    
# Finally transfer from charging account to the interest one
# The charging one should charge and the interest one add
# interest
    print ("C = ", c.checkBalance())
    print ("D = ", d.checkBalance())
    d.transfer(20,c)
    print ("C = ", c.checkBalance())
    print ("D = ", d.checkBalance())
	
