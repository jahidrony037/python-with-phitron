# another pattern problem 

for row in range(7):
    for col in range(row+1):
        print(chr(97+row), end=" ")
    print()