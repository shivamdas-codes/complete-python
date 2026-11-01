print("hello world ","im here") 
print("0303")
print(33)
# first 2 codes represent about how functions and strings are combined and give the proper output
# third code represent that the numeric value can be written inside the "" or weitten eithout the ""

print("hello world")
# first hello world printed sucessecfully

print(35+75)
print(54*34)
# first code represents sum of 2 values given
# second code represents product of 2 values

name = "shivam das"
age = 21
# the value which was written inside the strings are assigned by some name and number that represents the value of the given variable 



name = "shivam"
print (name[0:3])
# the above code says about the lenght of the string in positive manner


print(name)
print(age) 
print(name,age)
print("hey iam",name,"my age",age)
# insted of printing name we can simply give the variable to print that given word or number
# the print statement can be done in single line also

name2 = name
print(name,age,name2)
print(name2)                                                                     
# the above code represents the assignment rule 
# that means storing the let side value to the right side value known as a=b

# in the above code the identifiers rule also takes place where the numeric value or any special character like under score, upper case, lower case and any digit can be assigned after the name 


name = "shivam"
age = 21
price = 4500.50

print(type(name))
print(type(age))
print(type(price))
print(type(name2))
# the above code represent the type of the data that were given inside the variable

print(type(name),type(age),type(price))


age = 21
old = True
a = None

print(type(old))
print(type(a))
print(type(old),type(a))
# the above code represents the boolean and none value inside the function type

a = 3
b = 4
sum = (a+b)
diff = (a-b)
print(sum,diff)
# the above code represents the sum and difference of two numbers



# EXPRESSION EXECUTION RULES (1 TO 8):
# RULE 1:
a,b = 2,3
txt = "@"
print(a*txt*b)
"""Rule:1 - The above code represents that the strings and the integers can be operate together by using the *
(THIS COMES UNDER EXPRESSION EXECUTION RULE)"""

# RULE 2:
a,b = "2",3
txt = "@"
print((a+txt)*b)

a,b = "2",3
txt = "@"
print(a+txt*b)

a,b = "2","3"
txt = "@"
print(a+txt+b)
"""Rule:2 - The above code represents that the string and string can be operated by using the +  
(THIS COMES UNDER EXPRESSION EXECUTION RULE)"""


# RULE 3:
a,b = 2,3
c = 4
print(a+b*c)
"""Rule:3 - the above code says that the numaric values can be operater with all the arthmetic operations
(THIS COMES UNDER EXPRESSION EXECUTION RULE)"""

# RULE 4:
a = 3
b = 2.5
c = (a+b,a-b,a*b,a/b,a%b)
print(c)
"""Rule:4 - the above rule says that the integer and float can be operated with all the arthmetic operations and returns the float value
(THIS COMES UNDER EXPRESSION EXECUTION RULE)"""

# RULE 5:
a = 2
b = 3
c = a/b
print(c)
"""Rule:5 - The above code represents the division between the 2 integers which gives the output as float 
(THIS COMES UNDER EXPRESSION EXECUTION RULE)"""

# RULE 6:
a = 5.9
b = 2
c = a // b
print(c)

num1 = -2
num2 = 3
num3 = num1 // num2
print(num3)
"""Rule:6 - The above code represents the floor division between the float and integer which gives the output as float
(THIS COMES UNDER EXPRESSION EXECUTION RULE)"""

# RULE 7:
a = 5
b = 2
c = a % b
print(c)

num1 = 27
num2 = 4
num3 = num1 % num2
print(num3)
"""Rule:7 - The above code represents the modulus operation between the 2 integers which gives the remainder value
(THIS COMES UNDER EXPRESSION EXECUTION RULE)"""

# ------------------------------------------------------------------------------------------------------------------------

#(1).write a program to input 2 numbers and print their sum, difference, product, quotient and remainder
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

sum_result = number1 + number2
difference_result = number1 - number2
product_result = number1 * number2
quotient_result = number1 / number2
remainder_result = number1 % number2

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Remainder:", remainder_result)

# ---------------------------------------------------------------------------------------------------------------------

#(2).write a program to input side of a square and print its area and perimeter
side1 = float(input("Enter the square side1: "))
side2 = int(input("Enter the square side2: "))
side3,side4 = int(input("Enter perimeter of the square side3: ")), (input("Enter perimeter of the square side4: "))

area = side1 * side1
print("square side:", side2 ** 2)
print("Area of square:", area)
print("Perimeter of square:", 4 * side3,4 * side4)

#(3).write a program to input 2 floating point numbers and print their average
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

the_average = (num1 + num2) / 2
print("Average:", the_average)
print("Average:", (num3 + num4) / 2)

# (5).write a program to input users first name and print its length
user_1 = input("first name :")
firstname = len(user_1)
print(firstname)
print(len(user_1))   # prints the length of the string