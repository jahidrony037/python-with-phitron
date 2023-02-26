# problem -5 
# check Armstrong number 

num = int(input("enter the number : "))
temp_num = num
num_len = len(str(num))
temp = num_len

sum = 0
while(num):
    rem= num%10
    sum += rem**(temp)
    num//=10

if(sum == temp_num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


#method 2

a = input("enter the number : ")
len_ = len(a)
sum = 0
for i in a:
    sum+=int(i)**len_

if(sum == int(a)):
    print("armstrong number")
else:
    print("not armstrong")