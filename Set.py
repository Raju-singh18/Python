
x={1,2,3,4,5,6}
print(x);
y={1,1,13,4,5,3,3,23,13}
print(y);

# Dictionary
z={}
print(type(z));

# Set
g=set();
print(g);

a={1,2,3,4,5}
b={4,5,6,7,8}
a.union(b)
print(a.union(b));
a.update(b)
print(a);
print(b);
a.remove(6)
print(a)
#! error
# a.remove(11)
#! not give error
a.discard(11)

a.pop()
print(a)

a.add(1)
print(a);

a.add(6)
print(a)

print(a.issuperset(b));
