# reading from a file:
f = open("file.txt", "r")

data = f.read(5)    #the value inside the read() inicates to read the first 5 letters in the text file.
read_line = f.readline()    #this line indicates to read the first line

print(data)
print(read_line)
print(type(data))
print(len(data))
f.close()



file = open("file.txt","r")
data1 = file.readline()
print(data1)
data2 = file.readline()
print(data2)

data3 = file.readline()
print(data3)
file.close()
# in the 3rd case the next line will show as empty beacause all the data is already read so there is no data left to read so it will show as empty line in the end.


# writing to a file:
file = open("file1.txt","w")
file.write("hello im intrested in open source......") #this will override the previous data in the file.
file.write("contributing to real world projects") #this will be added to the previous line without any space or new line.
file.write("\nhey there how are you") #this will be added to the previous line with a new line.
file.close()

# appending to a file:
file = open("sample.txt","a")   #if there is no file with the name sample.txt it will create a new file with that name.
file.close()


# read and write both:    r+
f = open("sample.txt", "r+")
# f.write("hey there how are you")  #this will write at the begining of the file.
f.write("hello")    #this will override the first 5 letters of the file.
data = f.read()   #this will read the file from where the write operation ended.
print(data)
f.close()

# read and write both: w+
f = open("sample.txt", "w+")
f.read()  #this will not read anything as the file is opened in write mode and the file is empty.
f.write("hello world")  #this will write "hello world" to the file.
f.close()

# read and write both: a+
f1 = open("sample.txt", "a+")
f1.read()  #this will not read anything as the file is opened in write mode and the file is empty.
f1.write("hey")  #this will append "hey" to the file.
f1.close()


# with statement: both for reading and writing
with open("sample.txt","r") as f:
    data = f.read()
    print(data)

with open("sample.txt","w") as f:
    f.write("writing using with statement")


# ----------------------------------------------------------------------------------------------------------------------------------------------------

# FILE INPUT/OUTPUT PRACTICE PROGRAMS:
# (37). write a program to create a text file and write multiple lines to it
f = open("demo.txt", "w")
f.write("hii everyone")
f.write("\nwe are learning file input/output\ni like python\ni love coding")
f.close()
# or
with open("practice.txt","w") as f:
    f.write("hello world\nthis is practice file")
    f.write("\nwe are learning file handling in python")


# (38).write a function that replace all occurrences of a word "python" with "java" in a text file 
def replace_word():
    with open("demo.txt", "r") as f:
        data = f.read()
    new_data = data.replace("python","java")
    print(new_data)
    with open("demo.txt","w") as f:
        f.write(new_data)
replace_word()


# (39).search if the word "learning" is present in the text file or not
def find():
    with open("demo.txt","r") as f:
        data = f.read()
        if "practice" in data:
            print("present")
        else:
            print("not present")
find()
# or
def search_word():
    word = "learning"
    with open("demo.txt", "r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("found")
        else:
            print("not found")
search_word()


# (40). write a function in which line of the file does the word "learning" occur first print -1 if the word is not found
def check_line():
    word = "learning"
    data = True
    line_no = 1
    with open("demo.txt","r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1
print(check_line())


# from a file containing numbers seperate by comma(,) print the count of the even numbers
# method1:
count = 0 
with open("demo.txt","r") as f:
    data = f.read()

    num = data.split(",")   #this method is used to seperate the values by using comma
    for val in num:
        if int(val) % 2 == 0:
            count += 1
print("The even numbers are:",count)

# or

with open("demo.txt","r") as f:
    data = f.read()

    num = ""
    for i in range(len(data)):
        if data[i] == ",":
            print(int(num))
            num = ""
        else:
            num += data[i]
