
s=int(input("Enter starting number:"))
e=int(input("Enter starting number:"))

for x in range(s,e):
    for i in range(2,x):
        if(x%i==0):
            break
    else:
        print(x,end="  ");
    