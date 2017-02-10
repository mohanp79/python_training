# unordered groups, only association is key-value pairs , keys has to be unique, these are also mutable

gradeDict = {'Kori':88, 'sandy':67,'Jenny':79}

print(gradeDict)

print(gradeDict['Kori'])

gradeDict['Kori'] = 89

print(gradeDict)

del gradeDict['sandy']

print(gradeDict)