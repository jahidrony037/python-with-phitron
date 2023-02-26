#more list method part -2

#pop() Removes and returns the last value from the List or the given index value.
a=[1,2,3,4,5]
a.pop()
print(a) #remove the last elements form the list 

#remove() Removes a given object form the List 
b=[1,2,3,4,5]
b.remove(3)
print(b)

#clear() removes all items form the list.
b=[1,2,3,4,5]
b.clear()
print(b)

#reverse() Reverse objects of the List in place.
b=[1,2,3,4,5]
#print(b[::-1])
b.reverse()
print(b)


#sort()  Sort a List in ascending, descending
b=[1,3,2,5,4]
b.sort() #for ascending order
b.sort(reverse=True) #for descending order 
print(b)

#max() Calculate maximum value of the list 
b=[1,2,3,4,5]
print(max(b))

#min() Calculate minimum value of the list
b=[1,2,3,4,5]
print(min(b))