# method 1
#function defination
def var_name(a,b):  #defination with parameters a and b
    result1 = a + b
    result2 = a - b
    print(result1,result2)  

    return result1,result2  # return is used to send a value back from a function to the place where it was called. 

var_name(5,10)  #printing the arguments with the given a and b
var_name(10,5)  #printing the arguments with the given a and b


# method 2
# function defination
def new_var(num1 , num2):   #parameters
    return num1 + num2

sum = new_var(10,17)    #function call, arguments
print(sum)


# method 3
def null_value():   #no parametres assigned
    print("hello")

output = null_value() #the value which doesn't return anything it is consider as 'none'
print(output)
null_value()    #function call nothing here....
# this function doesnt return anything so python takes it as "NONE"

# -------------------------------------------------------------------------------------------------------------------------


# average of three numbers:
def numbers(a,b,c):
    average = a + b + c / 3
    print(average)

    return average
numbers(5,6,7)



# default parameters:
# example1:
def new_var(a,b):
    print(a*b)
    return(a*b)
new_var() 
# in this case it will always throw error because we didn't give any kind of arguments here

# example2:
def new_var(a=2,b=4):
    print(a*b)
    return(a*b)
new_var()
# in this case if we dont assign any arguments then it will take the parameters as the default value 

# example3:
def new_var(a ,b=4):
    print(a*b)
    return(a*b)
new_var(6)
# in this case it will take both arguments and the default value which is already assign in the "b" parameter
# if we dont assign any value in the arguments still it will take the default value which is already assigned.


# example4:
# def new_var(a=2,b):
#     print(a*b)
#     return a*b
# new_var(5)
# this case is different from the above case and it will throw error because...........non-default should come first and default should come next.



# --------------------------------------------------------------------------------------------------------------------------------
# FUNCTIONS PRACTICE PROGRAMS:
# (31).write a program to print the lenght of a list (hint:list should be in parameters)
cities_list = ["hyderabad", "odisha", "mumbai", "chennai"]
states_list = ["odisha", "telangana", "punjab", "karnataka","maharastra"]
def find_len(list): #here we can take any thing as parameter because in the above we already gave the list as variable and its values 
    print(len(list))    #now print the above parameter
    return cities_list
find_len(cities_list)   #call the original variables or we can call the given parameter as well.
find_len(states_list)   #call the original variables or we can call the given parameter as well.

def new_list(a,b,c,d):
    sum = a+b+c+d
    find_len = len(str(sum))
    print(sum)
    print(find_len)
    return sum
new_list(1,2,3,4)


# (32).write a function to print the elements of a list in a single line
list1 = ["a","b","c","d"]
list2 = ["1","2","3","4"] 
def elements(list):
    for i in list:
        print(i, end = " ")

    # print(list, end = "\n")
    # return list
elements(list1)
# elements(list2)


# (33).write a program to find the factorial of n
n = int(input("enter a number:"))
def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
    return fact
cal_fact(6) #calling function is mandotory no matter what value u have given in first variable or variable is there or not.


# (34).write a program to convert USD to INR
value = int(input("enter the value:"))
def converter(usd_value):
    inr_value = usd_value * 83
    print(usd_value, "USD =", inr_value, "INR")

converter(value) 