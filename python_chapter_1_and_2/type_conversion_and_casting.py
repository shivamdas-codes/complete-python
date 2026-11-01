# TYPE CONVERSION
a = 4
b = 2.5
c = a + b
print(c)
# this is the right apporch to wirte the type conversion
# if we write using string it will give error for eg:
# a = "2"
# b = 4
# c = a + b
# print(c)



# TYPE CASTING
a,b = 4, "2"
c = int(b)
sum = a + c
print(sum)

# or
a,b = 4, "2"
c = float(b)
sum = a + c
print(sum)

# or
a,b = 4, "2.5"
c = float(b)
sum = a + c
print(sum)

# or
a = int("2")
b = 4.5
c = a + b
print(c)

# or
a = float("2.5")
b = 4
print(type(a),type(b))
c = a + b
print(c)