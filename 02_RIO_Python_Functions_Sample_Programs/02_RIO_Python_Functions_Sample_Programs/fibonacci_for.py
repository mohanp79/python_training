#!/usr/bin/python 
import sys

def main():
	n = int(input("How many numbers of the sequence would you like? "))
	fibonacci(n)

def fibonacci(n):
	a, b = 0, 1
	for i in range(0,n):
		print (a)
		a, b = b, a + b
		
main()

