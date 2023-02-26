# Reverse a number 

num = int(input("Enter a Number : "))
reverse_num = 0
while(num):
    digit = num%10
    reverse_num = reverse_num*10 + digit
    num//=10

print(reverse_num)
