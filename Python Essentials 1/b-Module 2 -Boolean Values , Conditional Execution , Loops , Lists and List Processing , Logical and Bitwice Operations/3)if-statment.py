#syntax :
"""
if True or False :
    do this if True #indentation
"""
#example 1
if 0:
    print(False)
if 1:
    print(True) 
#example 2
if False :
    print(False)
print("hello")
#practice :
""" 
Write a program that asks the user to check whether a number is even or odd
, and whether it is greater than 100 or smaller.
""" 
#solution 
x = int(input("enter a integer number :"))
if x % 2 == 0 :
    print(x , "is even")
if x % 2 == 1 :
    print(x , "is od")
if x > 100 :
    print(x , " is greater than 100")
if x < 100 :
    print(x , "is smaller than 100")
if x == 100 :
    print(x , " is equal 100")