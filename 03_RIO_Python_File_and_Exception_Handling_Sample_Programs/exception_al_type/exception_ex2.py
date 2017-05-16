try:
	x = int(input('Enter the first number: '))
	y = int(input('Enter the second number: '))
	z = x + y
	print (z)
	print (x/y)
	print (z)
except ZeroDivisionError:
 	print ('''The second number can't be zero!''')
except TypeError:
	print ('''That Number is not Integer''')
except NameError:
        print ('''Name Error''')
