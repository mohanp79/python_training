# Fibonacci numbers module



def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    print("inside the fib2:",result)
    return result

n = int(input('Please Enter an Integer Number to calculate the Fibonacci numbers:'))

fib(n)

fib2(n)
