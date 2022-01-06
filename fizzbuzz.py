# If a number is divisible by 3, print 'Fizz'
# If a number is divisible by 5, print 'Buzz'
# If divisible by both 3 & 5, print 'FizzBuzz'
# Else just print the number.
#
# 1st line : number of test cases
# 2nd line : space separated upper limts for the test cases.
# lower limit is always 1
#
# Example input:
# 2
# 3 15
#
# Output:
# 1
# 2
# Fizz
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!! WRITTEN IN PYTHON 2 !!!!!!!!!!!!!!!!!!!!!!!!!!!

t = int(input())

upperLimits = [int(x) for x in raw_input().split()]

for ul in upperLimits:
    for i in range(1, ul+1):
        toPrint = i
        if i % 3 == 0 and i % 5 == 0:
            toPrint = 'FizzBuzz'
        elif i % 3 == 0:
            toPrint = 'Fizz'
        elif i % 5 == 0:
            toPrint = 'Buzz'
        print '%s\n' % toPrint
