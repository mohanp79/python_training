import csv
import re


File_UiName = open("D:\\Kannappan\\Automation_Scripts\\Python\\CTS_Python_training\\Samp\\new_2.txt", "r")
File_UiName_LogicPace = File_UiName.readlines()
Log_File = open("D:\\Kannappan\\Automation_Scripts\\Python\\CTS_Python_training\\Samp\\new_2_log.txt", "w")

for line_num,line in enumerate(File_UiName_LogicPace,1):

       #if line_num<=277 and line_num>=262:
        
                         if 'UiName=' in line:
                                 Log_File.write(line)
                                 #print(line)
                                 
                         if 'ConfigUsp=' in line:
                                #str.splitlines( num=line.count('\n'))
                                
                                PaceType=line.split('\\r\\n')[34].split('"')
                                #print (PaceType[1])
                                #print(PaceType)
                                Log_File.write("RunLogicPaceType: ")
                                Log_File.write(PaceType[1])
                                Log_File.write("\n")
                                if PaceType[1] == "Random":
                                        RunLogicRandomPaceMax=line.split('\\r\\n')[30].split('"')
                                        RunLogicRandomPaceMin=line.split('\\r\\n')[43].split('"')
                                        Log_File.write("RunLogicRandomPaceMax: ")
                                        Log_File.write(RunLogicRandomPaceMax[1])
                                        Log_File.write("\n")
                                        Log_File.write("RunLogicRandomPaceMin: ")
                                        Log_File.write(RunLogicRandomPaceMin[1])
                                        Log_File.write('\n')
                                        
                                elif PaceType[1] == "Const":
                                        RunLogicPaceConstTime=line.split('\\r\\n')[29].split('"')
                                        Log_File.write("RunLogicPaceConstTime: ")
                                        Log_File.write(RunLogicPaceConstTime[1])
                                        Log_File.write('\n')
                                        

File_UiName.close()
Log_File.close()
                         
                                
               
            


