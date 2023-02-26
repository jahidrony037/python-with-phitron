# problem 3 
# fibonacci series

num = int(input("Enter the Number : "))
first = 0
second = 1
for i in range(0,num+1):
    print(first, end=" ")
    res = first + second
    first = second
    second = res 
