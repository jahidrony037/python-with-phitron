#list built in methods

a =[1,2,3]
b =[4,5,6]
c= a+b
print(c)

#list convert string to list
s = "Helloworld!"
print(list(s)) #list function


#append() Adds an element at the end of the list
a=[12,24,13,45]
a.append(40)
print(a)
a.append(100)
print(a)
a.append("string")
print(a)


#insert() Adds an element at the specified position
a=[1,2,3,4,5]
a.insert(0,6) #(index_number, value)
print(a)

#copy() Returns a copy of the list
a=[1,2,3,4,5]
b=a.copy()
print(b)

#count() Returns the number of elements with the specified value
a=[1,22,2,3,4,2,2,2,3]
print(a.count(22))

#extend() merge any other list
a=[1,2,34]
#a.extend([12,14])
a= a + [12,14]
print(a)