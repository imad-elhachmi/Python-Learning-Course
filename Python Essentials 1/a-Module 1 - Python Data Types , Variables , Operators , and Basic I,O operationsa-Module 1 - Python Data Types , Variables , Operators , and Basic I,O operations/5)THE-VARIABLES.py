#variables naming conventions 
#- a variable name must contain UPPERCASE or lowercase letters , numbers , and the under score character _ (_ is a letter )
#- dont start with a number 
#- in python : VARIABLE != variable != Variabler ......
#- dont use reserved keywords 
#- use meaningful name
#- it does not contain a space
#-in python reservrd keywords : while != WHILE != .....
var1 = 1
print(var1) # 1
var1 = var1 + 1
print(var1) # 2
var = 7
print(var + 3) #10
version_python = "3.8.5"
print("Python" + version_python)
#f-string : f : Merge variables within texts
name = "imad"
age = 19
print(f"hello {name} your age is {age}") #hello imad your age is 19
                        #practice
#python theorem : c = ( a^2 + b^2 )^1/2
                        #solution
a = 6
b = 3
c =  ( a**2 + b**2 )**1/2
print(c)