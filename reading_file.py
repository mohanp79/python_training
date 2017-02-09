readFile = open('example_file.txt','r').read()
print(readFile)

splitFile = readFile.split('\n')

print(splitFile)
print(splitFile[1])

readFile2 = open('example_file.txt','r').readlines()
print(readFile2) # prints \n in the array as new lines are there