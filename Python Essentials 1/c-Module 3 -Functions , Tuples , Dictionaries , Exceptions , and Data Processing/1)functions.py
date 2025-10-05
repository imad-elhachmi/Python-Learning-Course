#syntax :
"""
def function_name():
    function body
    #return 
"""
#--------------------------------------------------------------------
def message():
    print("the function is runing")

#function call
print("we start here")
message()
print("we end here.")
#
def value():
    print("enter a value:")
value()
a = int(input())
value()
b = int(input())
print(f"{a}+{b}={a+b}")
#-------------------------------------------------------------------
#Returning a result from a function : return
#return the function to the location from which was called with or not value
"""
def function_name():
    return expression or not expression
"""
def calc():
    a , b = 3 , 3
    sum = a + b
    return sum
print(calc())#6

def hello():
    return 'hello'
mess = hello()
print(mess) #hello
#-----------------------------------------------------------------
#parameter functions
#syntax
"""
def function_name(optional parameters):
    the body of the function
"""
def hi(name):
    print("hi",name)
hi("imad")

def ft_addition(a , b):
    y = a + b
    print(y)
x , y = 2 , 9
ft_addition(x,y) 
#another method :
def ft_subtruction(last_number , first_number):
    print(last_number+first_number) 
ft_subtruction(first_number = 2 , last_number=7)
#NOTE :
""" 
def function_name(par1,par2,....,parn):
    body of function
function_name(val1,val2,....,valn)
"""
"""
def function_name(a,b):                          def function_name(a,b):
                       #True                                              #False
functipon_name(5,b=2)                            function_name(5,a=4)          
"""

#NOTE :
def function_name(a=5):
    print(a) #output is 3
function_name(a=3)

#NOTE :types the functions
#buit-in-function : print(),input()...
#user-defined-function 
#....
