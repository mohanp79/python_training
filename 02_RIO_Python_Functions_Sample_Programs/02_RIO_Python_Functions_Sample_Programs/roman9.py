"""Convert to and from Roman numerals """

import re

#Define exceptions
class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass

#Roman numerals must be less than 5000
MAX_ROMAN_NUMERAL = 20

#Define digit mapping
romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

#Create tables for fast conversion of roman numerals.
#See fillLookupTables() below.
toRomanTable = [ None ]  # Skip an index since Roman numerals have no zero
fromRomanTable = {}

def toRoman(n):
    """convert integer to Roman numeral"""
    if not (0 < n <= MAX_ROMAN_NUMERAL):
        raise (OutOfRangeError, "number out of range (must be 1..4999)")
    if int(n) != n:
        raise (NotIntegerError, "non-integers can not be converted")
    return toRomanTable[n]

def fromRoman(s):
    """convert Roman numeral to integer"""
    if not s:
        raise (InvalidRomanNumeralError, 'Input can not be blank')
    if not s in fromRomanTable:
        raise (InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % s)
    return fromRomanTable[s]

def toRomanDynamic(n):
    """convert integer to Roman numeral using dynamic programming"""
    assert(0 < n <= MAX_ROMAN_NUMERAL)
    assert(int(n) == n)
    result = ""
    """Here's where your rich data structure pays off, because you don't need any special logic to handle the
    subtraction rule. To convert to Roman numerals, you simply iterate through romanNumeralMap looking for
    the largest integer value less than or equal to the input. Once found, you add the Roman numeral representation
    to the end of the output, subtract the corresponding integer value from the input, lather, rinse, repeat."""
    for numeral, integer in romanNumeralMap:
        if n >= integer:
            result = numeral
            n -= integer
            print ('subtracting', integer, 'from input, adding', numeral, 'to output')
            break  
    if n > 0:
        result += toRomanTable[n]
    return result

def fillLookupTables():
    """compute all the possible roman numerals"""
    #Save the values in two global tables to convert to and from integers.
    for integer in range(1, MAX_ROMAN_NUMERAL + 1):
        romanNumber = toRomanDynamic(integer)
        toRomanTable.append(romanNumber)
        fromRomanTable[romanNumber] = integer
        print(toRomanTable)
    
fillLookupTables()
