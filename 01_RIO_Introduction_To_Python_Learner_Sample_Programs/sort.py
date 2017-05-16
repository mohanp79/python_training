from operator import itemgetter, attrgetter
Emp_tuples = [
        ('Ram', '2955', 5000),
        ('Arun', '2934', 3000),
        ('Biju', '2875', 10000),
]
print (Emp_tuples)
print ("Sort by Emp Salary: ")
print (sorted(Emp_tuples, key=lambda employee: employee[2]))   # sort by Salary
print ("Sort by Emp ID: ")
print (sorted(Emp_tuples, key=lambda employee: employee[1]))   # sort by EMP ID
print ("Sort by Emp Name: ")
print (sorted(Emp_tuples, key=lambda employee: employee[0]))   # sort by EMP Name


data = [(1,2,8), (4,1,10), (7,8,2)]
sorted_by_second = sorted(data, key=lambda tup: tup[1])
print("sorted_by_second: ",  sorted_by_second ) # Sorts based on the second element in the tuples

sorted_by_last = sorted(data, key=lambda tup: tup[2])
print ("sorted_by_last: ", sorted_by_last)

sorted_by_last_reverse = sorted(data, key=itemgetter(2), reverse = True)
print ("sorted_by_last_reverse: ",sorted_by_last_reverse)



