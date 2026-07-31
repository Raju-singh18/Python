
l1=[11,22,33,44,55]
print(l1)
print(type(l1))
for i in l1:
    print(i,end="  ")


l2=[55,"Amit",7.8, 7+8]
print(type(l2));
print(l2)
print(l2[0])
print(l2[1])
print(l2[2])
print(l2[3])

f='''x'''
# print(f)

x=[22,51,33,44,55]
x.append(66)
print(x)
x.insert(1,34)
print(x)
print(len(x))
# print(x.sort()) // output=None
print(x)
print(x.count(33))
print(x.index(22))
x.remove(33)
print(x)
print(x.pop(2))

# Slicing operator
x1=[66,34,55,91,24,23,54]
print(x1[2::])
print(x1[2:5])
print(x1[:4:])
print(x1[-1:-5:-1])
x1[0]=77
print(x1);

y="Aniket"
print(y[2])
print(y[3])
# print(y[-1::-1]) //reverse string
