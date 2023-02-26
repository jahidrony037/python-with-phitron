firstNumber = int(input("First Number : "))
secondNumber = int(input("Second Number : "))
thirdNumber = int(input("Third Number : "))

if firstNumber> secondNumber and firstNumber>thirdNumber:
    print("large number is ", firstNumber)
elif secondNumber>firstNumber and secondNumber>thirdNumber:
    print("large number is ", secondNumber)
else:
    print("large number is ",thirdNumber)