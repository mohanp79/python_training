# new in python 3

'''
name = input("What's your name? :")
print('Hello',name)
'''

import statistics

example_list = [2, 4, 5, 8, 21, 9, 17, 23, 12]

x = statistics.mean(example_list)
print(x)

x = statistics.median(example_list)
print(x)

x = statistics.mode(example_list)
print(x)

x = statistics.stdev(example_list)
print(x)

