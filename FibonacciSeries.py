
x=int(input("Enter a range:"));
p=0;
q=1;
print(p,end="  ")
print(q,end="  ")

# while x>2:
#     r=p+q
#     print(r,end="  ")
#     p=q
#     q=r
#     x=x-1;

for i in range(2,5):
     r=p+q
     print(r,end="  ")
     p=q
     q=r

s=-1
t=1
for i in range(x):
     u=t+s
     print(u)
     s=t
     t=u;
