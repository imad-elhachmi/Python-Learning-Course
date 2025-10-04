#syntax :
"""
if condition1:
    # code block if condition1 is true
elif condition2:
    # code block if condition2 is true
elif condition3:
    # code block if condition2 is true
elif condition4:
    # code block if condition2 is true
    .
    .
    .
else:
    # code block if none of the above conditions are true

"""
#example :
n , a = 10 , 10
if n > a :
    print("n > a")
elif n < a :
    print("n < a" )
else :
    print("n = a")

# exit() : The exit() function is used to terminate the program or end the current Python session
n = -1
if n == -1 :
    exit()
print("hello") #it will not print
