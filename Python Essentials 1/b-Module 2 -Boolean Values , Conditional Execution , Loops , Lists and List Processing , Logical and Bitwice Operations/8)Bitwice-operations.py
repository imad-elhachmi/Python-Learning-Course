#Method to Know the Bit Length of a Number in Python:the function : bit_length()
a , b = 10 , 1435
print(a.bit_length()) #4
print(b.bit_length()) #11
# decimal  back to binary : the function : bin()
print(bin(10)) #0b1010 the binary of 10 is 1010
#----------------------bitwise operations----------------------------------------------------------

#------------Bitwice and : & -> 0  & 1 = 0 , 1 & 0 = 0 , 0 & 0 = 0 , 1 & 1 = 1
                                                             #####################################
a = 5 #101                                                   #  1 0 1 
b = 3 #011                                                   #  0 1 1
result = a & b #001 = 1                                      #= 0 0 1 in decimal base is 1
print(result) # 1                                            #####################################

x , y = 55 , 100 #110111 , 1100100 #############################
res = x & y                        #  1 1 0 0 1 0 0
print(res)   # 36                  #    1 1 0 1 1 1 
                                   #=   1 0 0 1 0 0 in decimal base is 36
                                   #############################

#-----------Bitwice or : | -> 1|0 = 1 , 0|1 = 1 , 1|1 = 1 , 0|0 = 0
n = 5 #101  ###########################
c= 3 #011  # 1 0 1
print(a|c) #|
            # 0 1 1
            #=1 1 1 in decimal base is 7
            ##########################

w , z = 105 , 200 #1101001 , 11001000       ######################
print(w | z)  #233                          #    1 1 0 1 0 0 1
                                            #|
                                            #  1 1 0 0 1 0 0 0
                                            #= 1 1 1 0 1 0 0 1 in decimal base is 233
                                            ######################

#---------- Bitwise Not: ~ -> ~x = -(x + 1) -> ~10 = -11 (0 becomes 1 and 1 becomes 0)
k = 10  # 00001010 → ~k = 11110101 → -11
print(~k)  # -11

#---------Bitwise XOR : ^ -> 0 ^ 1 = 1 , 1 ^ 0 = 1 , 1 ^ 1 = 0 , 0 ^ 0 = 0
d , e =  5 , 3 # 101 , 011  ###############################
print(d^e) #6               #  1 0 1 
                            #^
                            #  0 1 1 
                            #= 1 1 0 in decimal base 6 
                            ##############################

f , g = 320 , 100 #101000000 , 1100100  #########################
print(f^g) #292                         #  1 0 1 0 0 0 0 0 0
                                        #^
                                        #      1 1 0 0 1 0 0
                                        #= 1 0 0 1 0 0 1 0 0 in decimal base is 292
                                        #########################

#--------------Bitwice shift : >>  <<
               #right shift :>>
#The bits in the binary are shifted to the right.
#The bits that come out from the right are deleted.
#Zero bits are added to the left.
h = 16 #10000
h>>=1 #01000 in decimal base is 8
print(h)

i = 166 #10100110
i>>=4 #00001010 in decimal base is 10
print(i)

               #left shift <<
#The bits in the binary number are shifted to the left.
#Zero bits are added to the right.
j = 5 #101
j = j << 1 #1010 in decimal base is 10
print(j) # 10

m = 166 #10100110
m = m << 5 #1010011000000 in decimal base is 5312
print(m)
#--------------NOTE :
"""
x&=y -> x = x & y ,  x|=y -> x = x | y
x^=y -> x = x ^ y ,  x>>=y -> x = x >> y
x<<=y -> x = x << y 
"""

