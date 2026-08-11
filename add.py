
# x=5
# def f1():
#     # x=7
#     # print(x); #7
#     # print(globals()['x']) #5
#     global x
#     x=7
#     print(x); 
# f1();


# x=int(input("Enter 1st Nummber: "));
# y=int(input("Enter 2st Nummber: "))
# def add(p,q):
#     return p+q;
# z=add(x,y);
# print("Addition is: ", z);

# ! positional arguments
# def amit(x,y=0,z=0):
#     print(x+y+z);
 
# amit(2,3,5)
# amit(2,5)
# amit(71)


#! keyword arguments 
# def fun1(x,y,z):
#     print(x)
#     print(y)
#     print(z);

# fun1(z=7,x=8,y=9)
# fun1(z=7,x=8,9) #gives error

# ! variable length arguments
# def fun2(*x):
#     print(x)
#     print(type(x))
#     x=list(x)
#     print(x)
#     print(type(x))

# fun2(10,12,30,40,50,60,70)
# ! Output
# (10, 12, 30, 40, 50, 60, 70)
# <class 'tuple'>
# [10, 12, 30, 40, 50, 60, 70]
# <class 'list'>

# def cricket(*runs, playername):
#     s=0
#     for i in runs:
#         s=s+i
#     print("Total runs: ",s, " made by ", playername);
# cricket(76,81,58,0,101, playername="Virat Kohli");
# cricket(45,70,99,49,1, playername="Rohit Sharma");


# def fun1(**p):
#     print(p);

# fun1(carname="maruti", year=2019, city="pune");
# fun1(empid=2,name="Ajit",age=21, height=175);

# ! output will be dictionary
# {'carname': 'maruti', 'year': 2019, 'city': 'pune'}
# {'empid': 2, 'name': 'Ajit', 'age': 21, 'height': 175}
