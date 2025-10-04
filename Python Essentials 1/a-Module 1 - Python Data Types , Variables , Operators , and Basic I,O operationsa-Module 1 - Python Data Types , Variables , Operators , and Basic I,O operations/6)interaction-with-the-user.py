#input() function : Taking data from the user*
anything = input("tell me anything :")
print(f"hmm...{anything}...really?")
#Practice : Write a program that asks the user to enter their name, age (as an integer), year of birth (as an integer), and the highest grade they achieved in their academic journey (as a float).
#solution :
name = str(input("enter your name :"))
age = int(input("enter your age : "))
year_of_brith = int(input("enter your year of brith : "))
highest_grade = float(input("enter your highest grade you achieved in their academic journey : "))
print(f"hi {name} : \nyour age is : {age}\nyear of brith is : {year_of_brith}\nhighest grade you achieved in their academic journey : {highest_grade} ")