# example program:
def show(n):    #given parameter as 'n'

    if n == 0:  #the recursion should perform till "0"                 "this is also known as BASE CASE"             
        return  #after completion of recursion it will return the value to the "n"
    """ in recursion the BASE CASE is very important if there is no base case then there is a chance that code will get crash """
   
    print(n)
    show(n-1)   #here the numbers will print in desending order.
    # show(n-1)
    # print(n)    #here it will print in ascending order.
show(5) #calling 5 as argument



# recursion using factoriol:
def fact(n):
    if n == 1 or n == 0:
        return 1    #default value
    return fact(n-1) * n    
print(fact(5))



# ---------------------------------------------------------------------------------------------------------------------------------------------------

# RECURSION PRACTICE PROGRAMS:
# (35).write a recursion function to calculate the sum of first 'n' natural numbers
def show(n):
    # sum = n(n+1)/2
    if n < 0: 
        print("not a natural numbers")
    if n == 0:
        return 0
    return show (n-1) + n
value = show(5)
print(value)


# (36).write a recursive function to print all elements in a list (use list and index as parameter)
# list = ["hyd", "mum", "odisha", "punjab", "AP"]
def show_list(list,index):
    if index == len(list):
        return 
    print(list[index])
    show_list(list, index + 1)  #index is increased by 1.
list = ["hyd", "mum", "odisha", "punjab", "AP"]
show_list(list,0) #'0' means from starting index
