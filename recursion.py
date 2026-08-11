# ! Run infinite times 
# def fun1():
#     print("Hello")
#     print("Bye")
#     fun1();

# fun1();


#! Sum of n number
# def sum(n):
#     if n==1:
#         return n
#     else:
#         return n + sum(n-1);

# print(sum(5));


# ! Factorial of n
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1);

p=int(input("Enter a number: "));
print(fact(p));
