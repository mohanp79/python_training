write_content = 'writing with help of program'

write_file = open('example_file.txt','w')

write_file.write(write_content)
write_file.close()

appendFile = 'appending text to existing file'

saveFile = open('example_file.txt','a')
saveFile.write('\n')
saveFile.write(appendFile)
saveFile.close()