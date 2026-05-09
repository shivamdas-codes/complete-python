# example: 1
dict = {
    "name" : "shivam das",                     # "KEY" is "STRING" and the "KEYVALUE" is "STRING"
    "age" : 21,                                # "KEY" is "STRING" and the "KEYVALUE" is "INTEGER"
    "marks" : 99.0,                            # "KEY" is "STRING" and the "KEYVALUE" is "FLOAT"
    "is_adult" : True,                         # "KEY" is "STRING" and the "KEYVALUE" is "BOOLEAN"
    "subjects" : ["python", "C", "java"],      # "KEY" is "STRING" and the "KEYVALUE" is "LIST"
    "topics" : ("dictionary", "sets"),         # "KEY" is "STRING" and the "KEYVALUE" is "TUPLE"
# in the dictionary the "keys" also can be written in the form of str(), int(), boolean() and tuple()
    }

print(dict["name"],dict["age"],dict["subjects"])
# if we want to print any particular value in the dictionary we can use   "print(dict["key"])"

dict["name"] = "shreya",
# if we want to replace any value we can use this   "dict["name"] = 'new value'"

dict["sur_name: "] = "das"
# if we want tp assign a new key and a new keyvalue we can use   "dict["newkey"] = 'new keyvalue'"

print(type(dict))
print(len(dict))
print(dict)



# example: 2
#  NESTED DICTIONARY
students = {
    "name" : "shivam",
    "subjects" : ["maths", "english", "science", "social"],
    "marks" : {
        "maths" : 99,
        "english" : 99,
        "science" : 99,
        "social" : 99,
    }
}
print(students)
# the above code represents "NESTED DICTIONARY", which means dictionary inside dictionary. 

print(students["marks"]["english"])
# if we want to print the dictionary which is present inside the dictionary then we can use this and we can also print the value which is inside the dictionary as well.



# METHODS IN DICTIONARY
# (1). keys()


# ----------------------------------------------------------------------------------------------------------------------------

# PRACTICE PROBLEMS ON DICTIONARY, SETS:

# (15).store the following word meaning in a pyhton dictionary
dictionary = {
    "cat" : "a small animal",
    "table" : ("a piece of furniture", "list of facts and figures"),

    "time_table" : {
        "breakfast" : "8:00 to 9:00",
        "lunch" : ("12:00", "to", "1:00"),
        "dinner" : [7,8] 
    }  #the syntax in the dictionary are very strict
}
print(dictionary)



# (16).you are given a list of subjects for students. assume one calssroom is required for 1 subject. how many classroom are needed by all students?
set1 = {"python", "java", "cpp", "python", "js"}
set2 = {"java", "python", "java", "cpp", "c"}
print(set1.union(set2))
# even the above code also written correctly but instead of finding lenght we assumed the subjects as 2 sets. 
print(len(set1.union(set2))) # by using the lenght function we can say that how many classrooms needed for each subjects.



# (17).write a program to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary and add one by one.use subject name as key and marks as value.
student_marks = {}  # an empty dictionary
subject1 = int(input("enter maths :"))
student_marks.update({"maths" : subject1})

subject2 = int(input("enter science :"))
student_marks.update({"science" : subject2})

subject3 = int(input("enter english :"))
student_marks.update({"english" : subject3})
print(student_marks)
#DOUBT: IF I GIVE SAME VARIABLE FOR ALL THE VALUES WILL IT OVER RIDE?
#NOTE: IF WE ENTER/GIVE THE SAME VARIABLE FOR THE ALL THREE INPUTS IT WILL TAKE SEPERATELY AND DONT OVERRIDE WITH EACH OTHER, THE OVERRIDE IS POSSIBLE WHEN THE KEY IS SAME NOT THE VARIABLE



# (18).figure out a way to store 9 and 9.0 as seperate values in a set.(hint: take help of builtin data types)
value = {9, 9.0}
print(value)
""" we know that the first value id integer and the second value is float
 in python it will take both the values as same values
 in set we cant print both the values as different values it will take both the values as the same number if that number is assigned by "0" after decimal"""

values = {9, "9.0"}
print(values)
# in this case we can able to print both the values as seperate values because one of the values is consider as string and the other as integer

values1 = {("float", 9.0),("int", 9)}
print(values1)
# in this case we can able to print our both the values because they were assigned by their original data types
# in this way also we can print two different values

