# the strings can be written in three ways
str1 = 'hello world'          # using single quotes
str2 = "hello world"          # using double quotes
str3 = '''hello world'''        # using triple quotes



# escape sequence in strings
str1 = "hey this is shivam das\ncurrently im pursuing my mca"
# the above line was assigned by '\n' which is used to break the line in the output as two sentences
str2 = "hey this is shivam das\tcurrently im pursuing my mca"
# the above line was assigned by '\t' which is used to give a tab space in the output
print(str1 )
print(str2 )


#1.concatenation of strings
str1 = "hello "
str2 = "world"
final_string = str1 + str2
print(final_string)


#2.lenghth of the string
str1 = "hello world"
print(len(str1))
str2 = "shivam das"
print(len(str2))
print(str1 + " " + str2)
print(len(str1 + " " + str2))


#3.indexing in strings
str1 = "hello world"
print(str1[0])   # first character
print(str1[4])   # fifth character
char = str1[6]
print(char)      # seventh character
# this is called positive indexing in strings 


"""# str = "hello world"
# str[5] =  'W'   # this will give error because strings are immutable in python
# print(str)"""



#4.slicing in strings
str = "hello world"
print(str[1:5])    # prints characters from index 0 to 4
print(str[5:11])   # prints characters from index 6 to 10
# this mainly used to get a substring from a given string

str2 = "shivam das"
print(str2[7:len(str2)])  # prints characters from index 7 to end of the string

str3 = "python programming"
print(str3[:6])   # prints 'python'
print(str3[7:])   # prints 'programming'
# this means if we don't provide starting index it will consider it as 0
# and if we don't provide ending index it will consider it as length of the string



# 5.negative slicing in strings
str = "hello world"
print(str[-5:-1])   # prints 'worl'
print(str[-11:-6])  # prints 'hello'
# negative slicing starts from the end of the string where -1 is the last character



# 6.string functions/methods
# ex:1 [endswith()]
str1 = "hello world"
print(str1.endswith("world"))   # returns True if the string ends with the specified suffix
print(str1.endswith("hello"))  # returns false if the string ends with the specified prefix


# ex:2 [capitalize()]
str2 = "hello world"
print(str2.capitalize())   # capitalizes the first character of the string

str3 = "python programming"
print(str3.capitalize())   # capitalizes the first character of the string 
print(str3)               # original string remains unchanged

str4 = "shivam das"
str5 = str4.capitalize()
print(str5)               # capitalized string is stored in a new variable


# ex:3 [replace()]
str1 = "hello world"
print(str1.replace("world", "python"))  # replaces 'world' with 'python'

new_str = str1.replace("hello", "hi")
print(new_str)                           # stores the replaced string in a new variable
print(str1)                             # original string remains unchanged


# ex:4 [find()]
str1 = "i love python programming"
print(str1.find("python"))   # returns the starting index of the first occurrence of the substring
print(str1.find("o"))     # returns the starting index of the first occurrence of the substring
print(str1.find("java"))     # returns -1 if the substring is not found


# ex:5 [count()]
str1 = "hello world hello"
print(str1.count("hello"))   # returns the number of occurrences of the substring
print(str1.count("o"))       # returns the number of occurrences of the character
print(str1.count("python"))   # returns 0 if the substring is not found


# ------------------------------------------------------------------------------------------------------------------------


# (6).write a program to find the occerrences of S in a string
str1 = input("enter string :")
count = str1.count("s")
print("Occurrences of 's':", count)   # prints the number of occurrences of 's' in the string

str2 = "this is shivam das"
print(str2.count("s"))   # prints the number of occurrences of 's' in the string