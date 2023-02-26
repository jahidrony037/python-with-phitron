# problem -1
# python program to print a multiplication table of a given number 

num = int(input("Enter the Number : "))

a=1
while(a<=10):
    r = num * a
    print(num ,"*", a ,"=", r)
    a+=1


print()

for res in range(1,11):
    print(num, "*", res, "=", num*res)