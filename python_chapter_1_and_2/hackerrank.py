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