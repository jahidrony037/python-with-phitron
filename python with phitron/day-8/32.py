#more about indexing 
#positive index start from 0,1,2....,n
#negative index start from -1,-2,-3,-......,-n

a = [15,14,20,1.5, "alu"]

a[0]=500
print(a[0])
print(a[-5])

if 500 in a:
    print("Found")
else:
    print("not found")

# ******* traversing *******

# for i in a:
#     print(i)

#positive indexing
# for i in range(len(a)):
#     print(a[i])

#negative indexing reverse elements 
# for i in range(-1,-len(a)-1, -1):
#     print(a[i])

#reverse elements print in list a 
# for i in range(len(a)-1,-1,-1 ):
#     print(a[i])


#nested list 
b=[[12,13], [18,23,"phitron"],[-1, -19]] 
b[0][0] = 200
b[1][2]= "joy"
print(b[1])