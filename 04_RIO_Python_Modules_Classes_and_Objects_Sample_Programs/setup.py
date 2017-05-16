from cx_Freeze import setup, Executable
import sys
import re

sys.argv.append('build')

exe = Executable(
      script="D:\\Kannappan\\Automation_Scripts\\Python\\CTS_Python_training\\Sample Programs\\fibo.py",
      base="Win32GUI",
      targetName="Fibo.exe"
     )


setup(
    name = "Fibo",
    version = "0.1",
    description = "I wish programming was this easy",
    executables = [exe])
