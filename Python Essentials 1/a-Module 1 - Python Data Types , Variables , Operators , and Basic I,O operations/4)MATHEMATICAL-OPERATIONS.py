#Exponent ** (x**y = x^y)
print(2**3) # 8
print(2**3.) # 8.0
print(2.**3.) # 8.0
#Multiplication * 
print(2. * 3.) #6.0
print(3 * 5 * 2) #30
#DIVISION / (ALWAYS RESULT IS FLOAT)
print(6/3) #2.0
print(6.3/3) #2.1
#Floor division // (ALWAYS RESULT IS INT ) (smallest correct value)
print(6 // 3) # 2
print(-6 // 3) # -2
#modulo  
print(2 % 2) #0
print(3 % 2) #1
print(975 % 10) #5
#ADDITION +
print(-4 + 4) #0
print(5 + 7 + 6.9 + 0.1) #19.0
#subtraction -
print(-6 -6) #-12
print(44 - 22) #22
#operators and their priorities
# 1) brackets () 2) exponent **(from left to right) 3)multiplication , division , floor division , modulo , (from left to right) 4) addition , subtruction (from left to right)
#2**2**(2**é) = 2**2**4 = 2**16 = 65536
#NOTE : in python :
#str + str = str and str + number is TypeError
print("hello" + " 2030") #hello 2030
#print("hello" + 44) #TypeError
#str * x = (Text repeats according to the value of x) and str * str = TypeError
print("hello" * 5)
print("P" * 45)
#print("hello" * "122") #TypeError
#Assignment operators (+= , /= , %= , -= , **= , //= , *= )
#   variable op= x is variable = variable op x 
var = 4
j = 10
var+=2*j # var = var + 2 * j 
print(var)
#the function : round(number , ndigits)
x = 122.27982
print(round(x,2)) #122.28
#NOTE :
#SCIENTIFIC NOTATION : ( e or E) XEZ = X*10^Z (Z is integer) (1.2E3 = 1.2*10^3 = 1200)
print(1.2E3) #1200.0
 
