year = int(input("Enter the year : "))

if (year%100 == 0 and year%400==0) or (year%4==0 and year%100!=0):
    print("leap year")
else:
    print("not leap year")