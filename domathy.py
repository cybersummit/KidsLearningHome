# Adds, multiplies, and divides two digits.
# Fixes the bug in the input function in Python 2.7 that allows for command injection.
from __future__ import division
try:
    input = raw_input
except:
    pass
A = input("Please enter your first number.")
B = input ("Please enter your second number.")
A = int(A)
B = int(B)
print("The first number is",  A)
print("The second number is", B)
print ("A + B=")
print (A+B)
print ("A * B=")
print (A*B)
print ("A/B=")
print (A/B)
# Trying format strings.
print ("%d / %d = %f"  % (A,B,A/float(B)))



