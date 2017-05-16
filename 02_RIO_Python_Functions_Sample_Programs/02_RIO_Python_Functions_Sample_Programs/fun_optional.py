def total(initial=5, *numbers, **keywords):
    """When we declare a starred parameter such as *param, then all the positional arguments
       from that point till the end are collected as a list called 'param'.
Similarly, when we declare a double-starred parameter such as **param, then all the
keyword arguments from that point till the end are collected as a dictionary called 'param'."""


    count = initial
    print("Initial Value is:", initial)
    print("Numbers: ",numbers)
    print ("Number of parameters: ", len(numbers))
    for number in numbers:
        print("Count value is: ", count)
        count += number
        print("Number in Numbers is: ", number)
    for key in keywords:
        print("Count value is: ", count)
        count += keywords[key]
        print ("Key in Keywords is: ", key)
    return count
print(total(10, 1, 2,25,43,23,89,12,21, vegetables=50, fruits=100))
