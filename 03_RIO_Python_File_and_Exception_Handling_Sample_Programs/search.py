import csv
import re


File_Path = open("D:\\Kannappan\\Automation_Scripts\\Python\\CTS_Python_training\\Samp\\new_1.txt", "r")
File_Path_Scripts = File_Path.readlines()
Log_File = open("D:\\Kannappan\\Automation_Scripts\\Python\\CTS_Python_training\\Samp\\new1_log.txt", "w")

for line_num,line in enumerate(File_Path_Scripts,1):
       if line_num >=10 and line_num<=38:
         #Find_All=re.findall('Path=',line)
         #print(Find_All)
         if 'Path=' in line:
                File_Name=line.split('\\')[-1]
                Log_File.write("Path: ")
                Log_File.write(File_Name)
                #Log_File.write('\n')
                #print(File_Name,line_num)
         if 'Scripts=' in line:
                        Scripts = line.split('=')[-1]
                        Log_File.write("Scripts: ")
                        Log_File.write(Scripts)
                        #Log_File.write('\n')
                        #print(Scripts,line_num)
               # print(File_Name)
File_Path.close()
Log_File.close()

                        


