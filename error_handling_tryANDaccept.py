
try:
    print('Running the try...')
    print(x)
    print('5'+x)

except TypeError as t:
    print('Type error occured')

except NameError as n:
    print('Name error triggered')

except Exception as e:
    print(str(e))
    print('General exception')

print('Code continues onward...')

