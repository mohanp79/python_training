from bankaccount_general import *
import time

# Create new function to generate unique id numbers
def getNextID():
    ok = input("Create account[y/n]? ")
    if ok[0] in 'yY':  # check valid input
       id = time.time() # use current time as basis of ID
       id = int(id) % 10000 # convert to int and shorten to 4 digits
    else: id = -1  # which will stop the loop
    return id
    
# Let's create some accounts and store them in a dictionary
accountData = {}  # new dictionary
while 1:          # loop forever
   id = getNextID()
   if id == -1: 
      break       # break forces an exit from the while loop
   bal = float(input("Opening Balance? "))  # convert string to float  
   accountData[id] = BankAccount(bal) # use id to create new dictionary entry
   print ("New account created, Number: ",id, "Balance: ",bal)

# Now let's access the accounts
for id in accountData.keys():
    print ("Account ID :", id, "Account Balance : ",accountData[id].checkBalance())

# and find a particular one
# Enter non-number to force exception and end program
while 1:
   id = int(input("Which account number? "))
   if id in accountData.keys():
      print ("Balance = ",accountData[id].checkBalance())
   else: print ("Invalid ID")
