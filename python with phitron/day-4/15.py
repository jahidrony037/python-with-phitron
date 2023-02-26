# For Loop range function and list function 


for item in range(10):
    print(item)

a = range(10)    # range function has three parameters (startIndex, endIndex, /)
print(a)
b=range(0,10)
print(b)
c = range(0,10,2)
print(c)
print(list(a))  # list function return a array list and  array elements are different types can be 
print(list(b))
print(list(c))

for i in range(100,-2,-2):
    print(i)

r =list(range(100,-2,-2))
print(r)