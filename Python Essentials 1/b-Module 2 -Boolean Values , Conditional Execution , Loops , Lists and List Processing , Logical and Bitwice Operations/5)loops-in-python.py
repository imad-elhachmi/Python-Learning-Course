                            #while loop :
# syntax
"""
initialization statement 
while condition :
    block of code 

    update expression
"""
# how work while loop
"""
A while loop in Python repeatedly executes a block of code as long as a given condition is true. 
Before each iteration,
the condition is checked—if it's true, the loop runs; if it's false, the loop stops.
"""
#practice 
i = 0
while i < 9 : 
    print(i)  # 0 1 2 3 4 5 6 7 8 9 (digits)
    i+=1

#infinite loop :
#while True :
#    print("help")
                            #foor loop
#the function range() : range(start,end,step)
x = range(9)
y = range(4 , 9)
z = range(0,11,2)
print(list(x)) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
print(list(y)) #[4, 5, 6, 7, 8]
print(list(z)) #[0, 2, 4, 6, 8, 10]
# how work for loop
##############################
# 1) First item --> Is this the last item?
#       No = True:
#           Execute expression
#           And
#           Get next item
#       Yes = False:
#           Execute expression
#           And
#           End for loop
##############################
#practice
for i in range(11) :
    print(i) # 0 1 2 3 4 5 6 7 8 9 10

for letter in "hello" :
    print(letter)  #h e l l o
 
