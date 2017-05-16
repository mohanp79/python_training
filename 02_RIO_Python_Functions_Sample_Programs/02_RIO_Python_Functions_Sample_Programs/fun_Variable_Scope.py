def func(x):
        print ('Inside the function',x)
        print ('x is', x)
        x = 2
        print ('Changed local x to', x)
        print ( 'Value of x is', x)
x = 50
print ('Outside the function:',x)
func(x)
print ('x is still', x)
