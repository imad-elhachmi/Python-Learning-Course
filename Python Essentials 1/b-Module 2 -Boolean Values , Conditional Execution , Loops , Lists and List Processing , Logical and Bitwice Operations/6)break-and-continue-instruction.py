                # the Break statement
#Stop and exit the loop when a certain condition is met
print("the Break statment :")
for i in range(11) :
    if i == 4 :
        break
    print(i)
print("outside the loop.")
# output 

            #the continue statement
#If a specific condition is met, skip the rest of the code in that iteration and start the next one
j = 0
while j < 10:
    if j == 4:
        j += 1
        continue
    print(j)
    j += 1
# output :
#0 1 2 3 5 6 7 8 9
