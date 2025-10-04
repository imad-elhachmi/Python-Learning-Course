# and : all conditions must be true
if True and 1 and 5==5 :
    print(True) #True

if (True and 5==5 and 6==8)==False :
    print(True) #true

# or : at least one condition is true
if True or False :
    print(True) #True

if (True or False or 5==7)==True :
    print(True) #True

# not : returns the inverse of the logical value
print(not(True)) # False
print(not(False)) # True