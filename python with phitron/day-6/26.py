#problem - 2

# Python program to find the factorial of a given number .

num = int(input("Enter the Number : "))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)