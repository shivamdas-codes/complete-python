# ARTHMETICAL OPERATORS 
# Example : 1
a = 10
b = 5
sum = (a+b)
diff = (a-b)
prod = (a*b)
div = (a/b)
mod = (a%b)
exp = (a**b)
print(sum)
print(diff)
print(prod)
print(div)
print(mod)
# we can write the arthmetic operator directly
a = 2
b = 4
print(a+b) 
print(a-b) 
print(a*b) 
print(a/b) 
print(a%b) 

# eg 2: SIMPLE INTEREST
# S.I = (P*R*T)/100
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
si = (p * r * t) / 100
print(si)   # written in optimized way.

# eg :3 
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
print((p * r * t) / 100)  # written in unoptimized way.



# RELATIONAL OPERATORS
a = 5
b = 10
print(a==b)
# equal to
print(a!=b)
# not equal to
print(a>b)
# greater than
print(a<b)
# less than
print(a>=b)
# greater than or equal to
print(a<=b)
# less than or equal to



# ASSIGNMENT OPERATORS/COMPOUND ASSIGNMENT OPERATORS
# we can write the assignment operator in 3 ways
a = 5
b = 10
a += b
print(a)
print(b)
# or
num = 5
num = num + 10
print(num)
# or
num = 5
num += 10
print(num)


# compound assignment operators examples......
num = 33
num += 7
print(num)
# add and assign
num = 33
num -= 7
print(num)
# subtract and assign
num = 33
num *= 7
print(num)
# multiply and assign
num = 33
num /= 7
print(num)
# divide and assign
num = 33
num %= 7
print(num)


# LOGICAL OPERATORS
a = 30
b = 20
print(not False)
print(not True)
print(a >= b)
# not operator gives the exact opposite of the boolean value

a = True
b = True
print(a and b)
a = True
b = False
print(a and b)
# and operator returns True only if both the operands are True other wise it returns false if one condition is False

a = True
b = False
print(a or b)
a = False
b = False
print(a or b)
a = True
b = True
print(a or b)
# or operator returns True if at least one of the operands is True otherwise it returns False if both conditions are False


# example program
a = 25
b = 35
print(not False)
print("and value :", a >= b and b >= a)
print("or value :", a >= b or b >= a)