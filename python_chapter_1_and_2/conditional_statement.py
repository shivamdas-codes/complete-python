# this code indicates about the conditional statements in python, which is mainly used in decision making
# example code 1
light = input("light colour =")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("get ready")
elif(light == "green"):
    print("go")
else:
    print("if light is broken")


# example code 2
marks = input("marks :")
if(marks >= "90"):
    print("grade A")
elif(marks >= "80" and marks < "90"):
    print("grade B")
elif(marks >= "70" and marks < "80"):
    print("grade C")
else:
    print("fail")
# in the above code the input statement always return the string not the integer value
# in the code the "and" operator is used to combine two conditions together


# example code 3
a = input("a :")
g = input("f/m :")
if((a == 2 or a == 1) and g == "m"):
    print("fee is 200")
elif(a == 3 or a == 5 or g == "f"):
    print("fee is 300")
elif(a == 4 and g == "m"):
    print("fee is 400")
else:
    print("no fee")



# this codes comes under ternary operator also known as the single line comment in python 
# we can write in two ways 
food = input("food :")
order = "yes" if food == "cake" else "no"
print(order)

# first by assigning the variable value in it 



# SINGLE LINE:
food = input("food :")
print("sweet") if(food == "cake" or food == "icecream") else print("not sweet")
# second by directly using print statement in it


# this code also part of the ternary operator but in different way, also known as the "clever if" statement
a = int(input("age :"))
vote = ("yes","no") [a >= 18]
print(vote)



# CLEVER IF:
# we can write a clever if statement in 2 ways...
sal = float(input("salary :"))
tax = sal *(0.1,0.2) [sal > 50000]
print(tax)

sal = float(input("salary :"))
tax = sal * (0.1 if sal <= 50000 else 0.2)
print(tax)



# part- 2
age = int(input("enter your age: "))
if (age < 18):
    print("you are a minor")
elif (age >= 18 and age < 65):
    print("you are an adult")
else:
    print("you are a senior citizen")



num = 100
if(num >= 2):
    print("true")
if(num < 10):
    print("true")   
if(num == 5):
    print("true")
elif(num != 5):
    print("false")
else:
    print("none")



voter_age = int(input("Enter your age: "))
if voter_age >= 18:
    print("You are eligible to vote.")
# if voter_age < 18:
#     print("You are not eligible to vote.")    
# elif voter_age == 18:
#     print("You have just become eligible to vote.")
else:
    print("Invalid age entered.")    

   

# NESTED IF STATEMENT
# example 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    citizenship = input("Are you a citizen? (yes/no): ")
    if citizenship.lower() == "yes":
        print("You can register to vote.")
    else:
        print("You must be a citizen to register to vote.")


# example 2
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Grade: A")
    if marks >= 95 and marks < 100:
        print("Excellent performance!")
        if marks == 100:
            print("Perfect score!")
elif marks >= 80 and marks < 90:
    print("Grade: B")
else:
    print("Good job!")


# # example 3
num = 75
if num % 5 == 0:
    if num % 2 == 0:
        print("java")
    else:
        print("python")
else:
    print("c++")


# SHORT CIRCUIT EVALUATION IN LOGICAL OPERATORS
years = 5
if True or False:
    years = years + 2
print(years)

# -----------------------------------------------------------------------------------------------------------------------

# to find wheather the numbers are positive,negative or zero
var = int(input("enter number:"))
if var > 0:
    print("positive")
elif var < 0:
    print("negative")
else:
    print("zero") 
# just normal code to find the single element is (+,- or 0)



num = int(input("enter a number:"))
if num % 2 == 0:
    print("even")
elif num % 2 != 0:
    print("odd")
else:
    print("the value is not a even not a odd")
# even or odd


num1 = input("enter a number:")
if num1.isdigit():  #this line only works if there is only strings that too any number inside the string.
    num1 = int(num1)
    if num1 % 2 == 0:
        print("its even")
    else:
        print("its odd")
else:
    print("not a valid number")
# even or odd with else statement



voting_age = int(input("enter your age:"))
if voting_age > 18:
    print("you are completely eligible to vote")
elif voting_age == 18:
    print("recently eligible \nyes you can vote")
else:
    print("dont waste time here \nyou are not eligible")
# eligible for voting or not



var = int(input("enter a number:"))
if var % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5 ")
# divisible by 5 or not



a = int(input("enter first number:"))
b = int(input("enter second number:"))
if a > b:
    print("a is largest number")
else:
    print("b is largest number")
# largest of two numbers

# ----------------------------------------------------------------------------------------------------------------------


num1 = int(input("number1:"))
num2 = int(input("number2:"))
num3 = int(input("number3:"))
if num1 > num2 and num1 > num3: #here num1 is greater than both num2 and num3
    print("num1 is largest")
elif num2 > num3 and num2 > num1:   #here num2 is greater than both num3 and num1
    print("num2 is largest")
else:
    print("num3 is largest")
# When comparing multiple numbers, each comparison must be explicit.    {for example: a>b and a>c}



char = input("enter any letter:")
vowels = ("a","i","o","u","e")
if char in vowels:
    print("this char is vowel")
else:
    print("not a vowel \nit is consonants")
# checking wheather the letter is vowel or not.



num = int(input("enter a number:"))
if num%3==0 and num%7==0:
    print("yes it is divisible by both")
else:
    print("not divisible")
# divisible by 3 and 7 or not.





number = int(input("enter a number:"))
if number == 2:
    print("prime number")
elif number == 3:
    print("prime number")
elif number > 1 and number % 2 != 0 and number % 3 != 0:
    print("ita a prime number")
else:
    print("its not a prime number")
# this conditions are not enough to find wheather to find a number is prime number or not.
"""doubt problem"""


# ----------------------------------------------------------------------------------------------------------------------------------


student_marks = int(input("enter marks:"))
if student_marks < 0 or  student_marks  > 100:
    print("invalid marks entered")
elif student_marks >=90 :
    print("GRADE A")
elif student_marks >= 75 and student_marks <= 89:
    print("GRADE B")
elif student_marks >= 60 and student_marks <= 74:
    print("GRADE C")
else:
    print("Fail")
# student marks and grades


# (7).write a program to input the grades of a students based on marks
student_marks = int(input("Enter your marks: "))
if student_marks >= 90:
    print("Grade: A")
elif student_marks >= 80 and student_marks < 90:
    print("Grade: B")
elif student_marks >= 70 and student_marks < 80:
    print("Grade: C") 
elif student_marks >= 60 and student_marks < 70:
    print("Grade: D")  
else:
    grade = "Fail"
    print("Grade:", grade)
    


# (8).write a program to check if a number is entered by the user is even or odd
num = int (input("Enter a number: "))
rem = num % 2
if rem == 0:
    print("The number is even.")
else:
    print("The number is odd.")



# (9).write a program to find the greatest among 3 numbers entered by the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1
    print("The greatest number is a:", num1)
elif num2 >= num1 and num2 >= num3:
    greatest = num2
    print("The greatest number is b:", num2)  
elif num3 >= num1 and num3 >= num2:
    greatest = num3
    print("The greatest number is c:", num3)
elif num4 >= num1 and num4 >= num2 and num4 >= num3:
    greatest = num4
    print("The greatest number is d:", num4)
else:
    print("All numbers are equal.")



# (10).write a program to check if a number is multiple of 7 or not
num = int(input("Enter a number: "))
rem = num % 7
if rem == 0:
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")
# or
a = int(input("Enter first number: "))
if a % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a multiple of 7")



# (12).write a program to check if a list contains a "palindrome" of elements (hint: use copy() method)
list1 = [2,3,3,2]  # this is a palindrome list
list2 = [5,6,4,1]  # this is not a palindrome list
list3 = ["m", "a", "a", "m"]

copylist1 = list1.copy()
copylist1.reverse()
# if you want to check wheather the given condition is palindrome or not first you have to copy() and then reverse() the given condition.
copylist2 = list2.copy()
copylist2.reverse()
# if you want to check wheather the given condition is palindrome or not first you have to copy() and then reverse() the given condition.
copylist3 = list3.copy()
copylist3.reverse()
# if you want to check wheather the given condition is palindrome or not first you have to copy() and then reverse() the given condition.
if (copylist1 == list1):
    print("its a palindrome")
else:
     print("not a palindrome")

if (copylist2 == list2):
        print("its a palindrome")
else:
    print("not a palindrome")

if(copylist3 == list3):
     print("its a palindrome")
else:
     print("not a palindrome")



#(4).write a program to input 2 int numbers, a and b print true if a is greater than or equal to b otherwise print false
var_a  = int(input("Enter first integer (a): "))
var_b  = int(input("Enter second integer (b): "))
if var_a >= var_b:
    print("True")
else:
    print("False")


# _________________________________________________________________________________________________________________________________________________________________

num = int(input("enter any number:"))
if num > 0:
    print("positive")
else:
    print("negative")


number = int(input("enter any number:"))
if number % 2 == 0:
    print("even")
else:
    print("odd")


num = int(input("enter a number:"))
if num % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5")


num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if num1 > num2:
    print("num1 is largest")
elif num2 > num1:
    print("num2 is largest")
else:
    print("both numbers are equal")


char = input("enter any character:")
vowels = ("a","e","i","o","u")
if char in vowels:
    print("this character is vowel")
if char == vowels[0] or char == vowels[1] or char == vowels[2] or char == vowels[3] or char == vowels[4]:
    print("this character is vowel")   
else:
    print("this character is consonant")

char1 = input("enter any character:")
if char1 == "a":
    print("this character is vowel")
elif char1 == "e":
    print("this character is vowel")
elif char1 == "i":
    print("this character is vowel")
elif char1 == "o":
    print("this character is vowel")
elif char1 == "u":
    print("this character is vowel")
else:
    print("this character is consonant")



age = int(input("enter the number:"))
if age >= 18:
    print("you are eligible to vote")
elif age == 18:
    print("you have just become eligible to vote")  
elif age > 1 and age < 18:
    print("you are not eligible to vote")
else:
    print("invalid age entered")

