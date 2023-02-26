#problem 3
# count digit number 

num=int(input("Enter the Number : "))
count=0
while(int(num)):
    num = int(num)//10
    count+=1
print(count)