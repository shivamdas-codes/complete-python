# (1).WHILE LOOP:

# while True:
#     print("hello")  
"""in this case the loop never stop at any point because the givenh value is always 'true'
if we want to stop loop at any point then the value should contain false at any point."""

while True:
    print("hello world")
    break
# this is the correct format to stop any infinite loop by using 'break' statement.



i = 1       # variable/iterator 'i' is assigned by 1
while i <= 5:   #loop performed till <=5
    print("hello")
    i += 1      #every time the loop takes place it will increase by "1" till 5
    print(i)    #this indicates how many times the loop has occured


j = 1
while j <= 100:
    print("hello world", j) # the 'j' represent that how many times the hello world will print
    j += 1
    print(j)    # this represent how many times the loops has occured



#DOUBT PROBLEM (1):
students_marks = 10
i = students_marks # we can able to change the variable to the new variable name. 
while i <= 48:
    print("need to improve", i)
    i += 2
students_marks = i # changed to the original name.
del i   # 'i' was deleted and no longer used in this code it is for temporary purpose.
print(students_marks)

#DOUBT PROBLEM (2): IMP FORMAT(HOW BOOLEAN VALUES WORK IN LOOP)
x = [True, True, (True+1)*4] # x = 10
y = False*3 + 1 # y = 1
# we know that in boolean "TRUE = 1" and "FALSE = 0"
for i in range(y + sum(x) - 9): #i is the variable here, the range(2)
    print(sum(x)+i) #though we know that the range is 2 we have to find the i value 2 times which is (10,11)



i = 1   # loop started 
while i <= 500: # loop will continue till assigned value and stopes when it reaches 'assigned value/false'
    print(i)
    i += 1
print("loop ended")



# BREAK STATEMENT()
password = "shiv@shre33"
while True:
    userinput = input("enter the password:")
    if userinput == password:
        print("LOGIN SUCCESFULLY\nWELCOME BUDDY")
        if userinput != password:
            print("NO PROBLEM\nTRY AGAIN")
        break
    else:
        print("STILL HOW MANY ATTEMPTS YOU WANT TO TRY \nDO ONE THING GO AND STUDY")


# CONTINUE STATEMENT():
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue    # when i=3 the loop will skip that value and continue the loop
    # basically when the value meets the condition it will not print that value and continue the loop 
    print(i)
    i += 1




# (2).FOR LOOP():
LIST = [1,2,3,4]
for i in LIST:  # each item of the list will be printed in a new line
    print(i)

name = "shivam"
for i in name:  # each letter will be printed in a new line
    print(i)

# for loop with else statement:
list = [1,2,3,4,5]
for i in list:
    print(i)
else:
    print("loop ended") #in this case after the loop ends the else statement will be executed which is not necessary


# for loop with break statement:
name = "shivam das"
for i in name:
    if i == "a":
        print("found")
        break
    print(i)
else:
    print("not found")

# for loop with continue statement:
name = "shivam das"
count = 0
for i in name:
    if i == "a":
        count += 1
        print("count is:",count)


# RANGE FUNCTION(): this is only used in for loop
for i in range(10): #this is the stoping point
    print(i)

for i in range(1,5):  # this is the starting and stopping point
    print(i)

for i  in range(1,11,2): # this is the starting, stopping and incrementing point (here 2 is the incrementing value)
    print(i)

# example: print("even numbers between 0 to 100 are:")
for i in range(10):
    if i % 2 == 0:
        print("even number:",i)

for i in range(0,100):  #starts from 0 to 99
    if i % 2 == 0:  # checks for even numbers
        print(i)

for i in range(0,100,2):  # starts from 0 to 99 with increment of 2
    print(i)
    

# pass STATEMENT():
for i in range(5):
    pass    #basically this statement is used when we dont want to write any code inside the loop but we want the loop to be there 
print("hii")


# --------------------------------------------------------------------------------------------------------------------------------------

# PRACTICE PROGRAM IN BOTH FOR LOOP AND WHILE LOOP:
# (19). print number from 1 to 100
i = 1
while i <= 100:
    print(i)
    i +=1


# (20). print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1


# (21). print the multiplication table of a number n
n = int(input("enter the number:")) # user input [ the input which is given is the fixed input and there is no change in that input]
i = 1       #starting point from where the loop will start and it can be changed
while i <= 10:  #ending point where the loop will end and it can be changed too
    print(n*i)  # 'n' is given input and 'i' is the variable which is changing every time
    i += 1
# so, basically we shouldn't assign the 'n' value in the loop because it is a fixed value and 'i' is the variable which is changing every time the loop takes place.


# (22). print the elements of a list using while loop
list = [1,4,9,16,25,36,49,64,81,100]
index = 0   # index always starts from 0
while index < len (list):  # len(list) = 10
    print(list[index])   # prints the element at the current index
    index += 1           # move to the next index


# (23).search for a number "x" in this tuple using loop
tuple = (1,4,9,16,25,36,49,64,81,100,1,4,9,16,25,36,49,64,81,100)
x = int(input("enter the number to search:"))
i = 0   #initialization
while i < len(tuple):
    if tuple[i] == x:
        print("found the index:",i)
    else:
        print("keep finding")   #it keeps finding till the last index though the value is found or not found
# its not nesassary to use the else statement in this case 
    i += 1


# (24).print the element of the following list using a for loop
list = [1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)


# (25). search for a number "y" in this tuple using for loop
tuple = (1,4,9,16,25,36,49,64,81,100,)
x = int(input("enter number:"))
idx = 0
for i in tuple:
    if i == x:
        print("found the number:", idx)
    idx += 1
# to find the index of the given number we have to create a new variable 'idx' and assign it by 0 and every time it should be increased by 1 till it matches the x value


# (26). print numbers from 100 to 1 using for loop
for i in range(100,0,-1):   #in 'step' section if we want to increase the value we have to give positive value and if we want to decrease the value we have to give negative value
    print(i)


# (27).print numbers from 1 to 100 using for loop
for i in range(1,101):
    print(i)


# (28). print the multiplication table of a number n using for loop
n = int(input("enter the number:"))
for i in range(1,11):
    print(n*i)
    print(f"{n} * {i} = {n*i}") #this line is the formatted string literal which is used to print the multiplication table in a proper format.


# (29). write a program to find the sum of first n natural numbers using both for loop and while loop
n = int(input("enter the value of n:")) #here 'n' is taken as 'i'
sum = 0 #starting/initial value of sum
for i in range(1,n+1):  #loop starts from (1 to n+1) because the range function exclude the last value
    sum += i
    print(sum)
# finding natural numbers using while loop

m = int(input("enter number:"))
sum = 0
i = 1
while i <= m:
    sum += i
    i += 1
print(sum)
# finding natural numbers using for loop
"""i have doubt here"""


# (30).write a program to print the factorial of a number using both for loop and while loop
n = int(input("enter the number:"))
fact = 1    #when we using factorial the starting value should be 1 because if we take 0 then the factorial will be 0
i = 1
while i <= n:
    fact *= i
    i += 1
print("the factorial is:", fact)
# factorial using while loop

m = int(input("enter the number:"))
fact = 1
for i in range(1, m+1):
    fact *= i
print("the factorial is:", fact)
# factorial using for loop




# (31). print numbers from 1 to n 
num = int(input("enter the number:"))
for i in range(1, num+1):
    print(i)

n = int(input("enter the number:"))
i = 1
while i <= n:
    print(i)
    i += 1


# # (31). print numbers from n to 1
num1 = int(input("enter the number:"))
for i in range(num1, 0, -1):
    print(i)

n1 = int(input("enter the number:"))
i = n1
while i >= 1:
    print(i)
    i -= 1
