list = [1,2,3,4,5,6,7,8,9,"hello",2.33]
print(list) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', 2.33]
#accessing list content : list[i]
print(list[0]) #1
print(list[9]) #hello
# the len() function : length
print(len(list)) #11
# how do you change the value of a chosen element in the list
list[0] = 200
list[1] = list[3]
print(list) #[200, 4, 3, 4, 5, 6, 7, 8, 9, 'hello', 2.33]
#how can you swap the values of two variables in python :
#x , y = y , x
#list[i] , list[j] = list[j] , list[i]
#removing elements from a list : instruction named del() : delet
del list[9]
print(list)#[200, 4, 3, 4, 5, 6, 7, 8, 9, 2.33]
#negative indices are legal :
print(list[-1],list[-2],list[-10]) #2.33 9 200
#adding elements to a list :
# the function append()
#syntax : my_list.append(value)
list.append(2000)
print(list) # [200, 4, 3, 4, 5, 6, 7, 8, 9, 2.33, 2000]
#the function insert() : syntax : my_list.insert(location,value)
list.insert(2,2030)
print(list) #[200, 4, 2030, 3, 4, 5, 6, 7, 8, 9, 2.33, 2000]
# sorting simple liste 
#the function sort() : syntax : my_liste.sort() : ascending order
list.sort()
print(list) #[2.33, 3, 4, 4, 5, 6, 7, 8, 9, 200, 2000, 2030]
list.sort(reverse=True) # descinding order
print(list)#[2030, 2000, 200, 9, 8, 7, 6, 5, 4, 4, 3, 2.33]
#the function reverse() : syntax : my_list.reverse() 
list.reverse()

my_list = [2,6,1,9,2,4]
my_list.reverse()
print(my_list) #[4, 2, 9, 1, 6, 2]
#------------------------------operations on lists 
#my_list[start:end]
#del my_list[start:end]
#del my_list[:] -> True : del my_list -> NameError
my_list2 = ["a","b","c","d","e"]
print(my_list2[1:4]) #['b', 'c', 'd']
del my_list2[1:4]
print(my_list2) #['a', 'e']
#the in and not in operators :syntax : element (in)or(not in)  (string)or(list)or(...)
lst = ['hello',"world",2030]
print("2030" in lst) #False
print("world" not in lst) #False
print(2030 in lst) #true
#-----------nested list
nested_list = [
    [5,3],
    [7,4,2],  # or this method nested_list = [[5, 3], [7, 4, 2], [4, 6], [3, 8, 9, 10]]
    [4,6],
    [3,8,9,10]
]
print(nested_list) #[[5, 3], [7, 4, 2], [4, 6], [3, 8, 9, 10]]
     #    0   #    1   #    2   #    3   #
#    #####################################
#  0 #    5   #   3    #        #        #
#    #####################################
#  1 #    7   #    4   #    2   #        #
#    #####################################
#  2 #    4   #    6   #        #        #
#    #####################################
#  3 #   3    #    8   #   9    #   10   #
#    #####################################
print(nested_list[3][2]) #9
#my_nested_list[number of line][number of colone]
#my_nested_list.append(new_list)
#my_nested_list[number of line][number of colone] = x
#del my_nested_list[number of line][number of colone]
#my_nested_list.insert(location,new_list)



