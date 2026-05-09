# example 1:
class student():
    name = "shivam das"

s1 = student()
print(s1.name)
s2 = student()
print(s2.name)
# basically both s1 and s2 are different objects of same class student but both have same attribute name as it is defined in the class once.


# example 2:
class car():
    color = "blue"
    brand = "BMW"

c1 = car()
print(c1.color)
print(c1.brand)



# example 3: (IMPORTANT)
class student:
    college_name = "avanthi institutes"
    name = "anonymous"  #class attr...........this is used in case any student name is not provided

    def __init__(self):
        pass
    # it is a default constructor
    # if we dont write any constructor then python provides a default constructor
    
    def __init__(self,name,marks):  # constructor with parameters
        self.name = name    #obj attr
        self.marks = marks
        print("adding new data to datebase")
    # it is a parameterized constructor

s1 = student("shivam",95)
print(s1.name,s1.marks)
print(student.college_name)

s2 = student("shreya",98)
print(s2.name,s2.marks)
print(student.college_name)



# example 4:
class student:
    college_name = "avanthi institute"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student", self.name, "to", student.college_name)

    def get_marks(self):
        return self.marks
    
s1 = student("shivam",95)
s1.welcome()
print(s1.get_marks())

s2 = student("shreya",98)
s2.welcome()
print(s2.get_marks())



# ABSTRACTION example:
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True #here the abstraction is implemented as we are hiding the internal details of how a car starts
        self.brk =  True    #here the abstraction is implemented as we are hiding the internal details of how a car starts
        self.clutch =  True #here the abstraction is implemented as we are hiding the internal details of how a car starts
        print("car started")

c1 = car()
c1.start()

# ---------------------------------------------------------------------------------------------------------------------------------------

# PRACTICE PROBLEMS:
# create student class that takes name and marks of 3 subjects as arguments in constructor. then create the method to print the average.
class student:
     def __init__(self,name,marks):
        self.name = name
        self.marks = marks

     def find_average(self):
        return sum(self.marks) / 3
     
s1 = student("shivam", [95, 90, 85])
print(s1.find_average())


# # or
class student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod   #this is a static method as it does not use any obj or class attr
    def college():
        print("avanthi institute")

    def find_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        print("hey", self.name, "your average marks is:", sum / 3)

s1 = student("shivam", [98,99,76] )
s1.find_avg()

s1 = student("shreya", [88,79,96] )
s1.find_avg()   #here we can change our attr directly if i is needed from outside the class.



#   CREATING AN ACCOUNT CLASS: (IMPORTANT) 
# create account class with 2 attributes -> balance and account number, now create method for debit and credit and printing the balance.
class account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance is {self.balance}.")

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Debited {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance
    
acc1 = account("123456789")
acc1.credit(500)
acc1.debit(200)
print("Current balance:", acc1.get_balance())

