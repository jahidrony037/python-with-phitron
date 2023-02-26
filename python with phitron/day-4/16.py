# more about for loop

a = "Hello World"
print(a)
for letter in a:
    print(letter) #print all letter of a string

bag = ["alu", "begun", "potol", "fish", "meat", 2,2,4.56, -345, 450]
for item in bag:
    print(item) # print all items individually from bag list

lst= [12,3,4,5,-3,-34, 0.45, 21]
for number in lst:
    if number<=10:
        print(number)

#  print the numbers between 1 to n which are divisible by 3 and 5

n=int(input("Enter the Number : "))
for number in range(1,n):
    if number%3==0 and number%5==0:
        print(number)


# sum between 1 to n num
sum = 0
for num in range(1,6):
    sum+=num
print(sum)