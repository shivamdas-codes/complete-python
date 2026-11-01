# (1).INFINITE LOOP EXAMPLE:
temp = 0
while temp <100:    # less than 100
    temp += 1       # increment by 1
    if temp == 100:
        temp = 0
# this is basically an infinite loop which never ends because when temp reaches 100 it is again assigned to 0.


# (2).EXPONENTIATION OPERATOR:
a = 2**3    # 2 raised to the power 3
b = a**2    # a raised to the power 2
print(b)
c = 2**3**2 # 2 raised to the power (3 raised to the power 2)
print(c)


# (3).BOOLEAN ARITHMETIC:
x = [True,True,(True+1)*4]  #true =1
y = False*3 + 1 #false=0
for i in range(y+sum(x)-9):
    print(sum(x)+i)


# (4).STRING SLICING:
s = "butterfly" # index started from 0 to 8
s = s[2:]   # index sliced from 2 to end
# now this become "tterfly"
s = s[:5] + s[-2]
# now take the first 5 char and last 2 char (this become "tterf" + "l" = "tterfl")
print(s)


# (5).FIND METHOD AND STRING SLICING:
string = "python"
print(string[string.find('t') + 3:])  # find the index of 't' and slice from that index +3 to end


# (6).BOOLEAN EVALUATION:
a = "1" # non empty string
b = "0" # non empty string
# the above assign values are string type that means both a and b are "True" because non-empty strings are considered True and empty strings are considered False in boolean context.
# if any interger is assign then assume "true = 1 , false = 0"
if a and b == True:
    print("its a true statement")
else:
    print("its a false statement")


# (7).TYPE CONVERSION:
a = int("11", 2) # binary to decimal conversion
print(a)


# (8).LIST REMOVAL DURING ITERATION:
my_list = [3,4,5,6,7] #THE ELEMENTS ARE ASSIGNED FROM INDEX 0 TO 4
for i in my_list:
# THIS LOOP FOLLOWS THE ELEMENTS ONE BY ONE FROM THE LIST AND REMOVES THEM
# EXAMPLE: my_list[0], my_list[1], my_list[2]....
    my_list.remove(i)
print(my_list)


# (9).FOR LOOP WITH RANGE AND ACCUMULATION:
x = 0
for i in range(3):#the range(0,1,2) now add one after one with x
# case(1): i=0 , x=0+0=0
# case(2): i=1 , x=0+1=1
# case(3): i=2 , x=1+2=3      finally i=2 and x=3
    x += i
print(i,x)


# (10).VARIABLE ASSIGNMENT AND MUTABILITY:
x = 0
y = x   # y is assigned the value of x which is 0
y += 1  # y is incremented by 1, now y=1 but x remains 0
print(x,y)


# (11).LIST SLICING WITH NEGATIVE STEP:
"""doubt"""
var = [1,2,3,4] #original list
new_var = var[::-2] #[start:end:step] follow this pattern if there is three slicing and the step is negative in this case which is -2.
new_var.append(9)
print(var)
print(new_var)


# (12).STRING METHOD isalpha():
a = "12"    #its a string not a number
if a.isalpha(): # checks if all characters in the string are alphabetic eg: 'abc' = true , '123' = false , 'abc123' = false
    print("true")
else:
    print("false")


# (13).NESTED CONDITIONAL STATEMENTS:
num = 75
if num % 5 == 0:
    if num % 2 == 0:
        print("java")
    else:
        print("python")
else:
    print("c++")


# (14).LIST SLICING WITH NEGATIVE INDICES:
num = [1,2,3,4]
print(num[-3:-1])   #negative slicing


# (15).DIVISION OPERATORS AND TYPE COMPARISON:
print(type(10/5) == type(10//5))    #first type is normal division and second type is floor division.float != int so the output is False


# (16).STRING SLICING WITH STEP:
str = "python"
print(str[1:4:2])  #string slicing with step remove 2(from index 1 to 4)


# (17).BOOLEAN ARITHMETIC WITH STRINGS:
a = True + True + False # True=1 , False=0
print(a * "Hello")  # 2 * "Hello" = "HelloHello"


# (18).FINDING CHARACTER POSITION IN STRING:
str = "abracadabra"
i = str.rfind('a')  # find the last occurrence of 'a' rfind = reverse find(from right to left)
print(str[i - 1])


# (19).BREAK STATEMENT IN LOOP:
for i in range(5):  # loop from 0 to 4
    if i == 2:  # when i equals 2 it consider as true then the loop stopes here.
        break
    print(i,end ="")


# (20).STRING METHODS AND LIST JOINING:
letters = ['a', 'b', 'c', 'd']
combo = '-'.join(letters).upper()
print(combo)


# (21).LIST MUTATION DURING ITERATION:
clcoding = [1,2,3,4]
total = 0
for x in clcoding:
    total += x
    clcoding[0] = total 
print(clcoding)


# (22).DICTIONARY VALUE ITERATION AND CONDITIONAL ACCUMULATION:
d = {'a':1, 'b':2, 'c':3}
s = 0
for v in d.values():
    s += v if v > 10 else 2
print(s)


# (23).LIST MODIFICATION DURING ITERATION:
nums = [1,2,3,4,5]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)


# (24).IDENTITY OPERATOR WITH LISTS:
a = [1,2,3,4,5]
b = [1,2,3,4,5]
if a is b:
    print("same")
else:
    print("different")


# (25).IDENTITY OPERATOR WITH LISTS - PART 2:
a = [1,2,3]
b = [1,2,3]
if a is b:  #is operator checks whether both a and b refer to the same object in memory.
    print("same")
else:
    print("different")



# (26).PRIME NUMBER CHECKER:
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



num1 = int(input("Enter first number: "))
if num1 == 2:
    print("its a prime number")
elif num1 % 2 == 0 or num1 < 1:
    print("its not a prime number")


"""(1).Given an integer, n , perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird"""

n = int(input())
if n % 2 != 0:
    print("weird")
elif n % 2 == 0 and n in range(2,6):
#elif n % 2 == 0 and 2 <= n <= 5:          we can write like this insted of writing "range(2,6)"
    print("not weird")
elif n % 2 == 0 and n in range(6,21):
#elif n % 2 == 0 and 6 <= n <= 20:         we can write like this insted of writing "range(6,20)"
    print("weird")
elif n % 2 == 0 and n > 20:
    print("not weird")

# or

n = 24
if(n is "odd" and "odd numbers are weird"):
    print("weird")
elif(n is "even" and n in range(2,5)):
    print("not weird")
elif(n is "even" and n in range(6,20)):
    print("weird")
else:
    (n > 20 and n is "even")
    print("not weird")

    

"""(2).The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers."""

a = int(input())
b = int(input())
sum = (a + b)
diff = (a - b)
prod = (a * b)
print(sum,diff,prod)



"""(3).The provided code stub reads two integers, a and b, from STDIN.Add logic to print two lines. 
The first line should contain the result of integer division, a // b. 
The second line should contain the result of float division, a / b.
No rounding or formatting is necessary."""

a = int(input())
b = int(input())
num1 = (a // b)
num2 = (a / b)
print(num1)
print(num2)



"""(4).The provided code stub reads an integer,n, from STDIN. For all non-negative integers i<n, print i square."""
n = int(input("enter the number:"))
i = 0
while i < n:
    print(i ** 2)
    i += 1
# or
m = int(input("enter the num again:"))
for i in range(m):
    print(i**2)
    i += 1