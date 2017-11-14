# My script is for learning with kids.
# Example of command injection in Python 2.7
from __future__ import division
from __future__ import print_function
# Fixes the bug in the input function in Python 2.7 that allows for command injection.
try:
    input = raw_input
except:
    pass
def test_types():
    print("Hello World")
    print(2+5)
    A=3
    A+=3
    print (type (A))
    B=11
    print(A+B)
    globals()
    A="Hailey"
    print (type(A))
    B=", welcome to Python!"
    print(A + B)
    C=100
    C = str(C)
    print (type(C))
    print ("5"+C)
    C = int(C)
    print (5+C)
    print (11/4.0)
def test_assign():
    a=30
    b="a"
    print(b)
    print("b")
    b=a
    print(b)
def test_print_py3print():
    print (300+5,"is the answer", "time",end=".")
def test_format_stirngs():
    print("Hi %10s How are you %s" % ("Hailey,", "Today"))
    print("I want $ %4d %s" % (1000000, "today!"))
def badinput():
    Z= input("What is your name?")
    # __import__("os").system("dir c:\ /s")
    print(Z)
#
badinput()







