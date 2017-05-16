try:
	print ('A simple task')
	x = input('Enter the first number: ')
	y = input('Enter the second number: ')
	print (int(x)/int(y))	
except:
	print ('What? Something went wrong?')
else:
	print ('Ah... It went as planned.')
