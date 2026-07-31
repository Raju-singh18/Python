
x1=(22,45,78,11,90,37)
print(type(x1))

x2 = 11,22,33,44,55,34,78
print(type(x2))

x3=43
print(type(x3))

x4=(66,)
print(type(x4))

x5=11,
print(type(x5))

print(x1);
print(x2);
print(x3);
print(x4);
print(x5);

print(x1.index(11))
list(x1);
print(list(x1))
x1=list(x1)
print(x1)

t1= 11,23,44,53,56,23
for i in t1:
    print(i)

l=len(t1)
x=0
while x!=l:
    print(t1[x])
    x=x+1
