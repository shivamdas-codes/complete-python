# eg: 1
tup = (3,4,5,6,8) #tuple values
print(type(tup))  #type of tuple
print(tup[0])
print(tup[1])
print(tup)
# tup[2] = 10    this represents assign or replace a new value with the old value, which is not valid in the tuples and immideatly it returns error.


# eg: 2
tup1 = () #an empty tuple
print(type(tup1))
print(tup1)
# this is absolutly valid in the tuples, we can assign the empty value in the tuples


# eg: 3
tup2 = (1,)  # single valuie in tuple
tup3 = ("hello",) # single value in tuple 
tup4 = (55.0,)
print(type(tup2), type(tup3), type(tup4))
print(tup2,tup3,tup4)
# we should write single element by using the(,) after the element, otherwise it does not take that value as the tuple.
# for example:
for_eg = (1)
for_eg1 = ("hello")
for_eg2 = (66.0)
print(type(for_eg),type(for_eg1),type(for_eg2))
print(for_eg,for_eg1,for_eg2)
# in this given example it does not take as tuple instead of this will take as the int(),str(),float() because the singlr element doesn't ends with the (,)


# SLICING IN TUPLES
# eg: 1 ( positive slicing )
tupple = (4,5,6,3,7)
print(tupple[1:4])
print(tupple[1:]) # takes empty as "lenght of the index till end"
print(tupple[:3]) # takes empty space as 0

# eg: 2 ( negative slicing )
tupple1 = (76,84,63,33,98,90)
print(tupple1[-4:-1])
print(tupple1[-5:])
print(tupple1[:-3])


# METHODS IN TUPLES
# (1). index()
num_list = (2, 7, 8, 4, 3, 8)
print(num_list.index(8))
# print(num_list.index(1))   in the index() method the elements which are present inside the tuple only prints as output if we try to give the element which is not in the list it will return as error.

# (2). count()
num_list2 = (4,6,3,5,3,5,6,3,3,3,7,3)
print(num_list2.count(3))
# this method is use to count that how many time an element is repeated



# ------------------------------------------------------------------------------------------------------------------------

# (13).write a program to count the number of students with the "A" grade in the following tuple
students_grades = ("A", "B", "C", "A", "A")
print(type(students_grades))   # type of the variable
print(len(students_grades))   #lenght of the variable
print(students_grades.count("A"))