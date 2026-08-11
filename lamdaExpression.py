
# r=lambda x,y: x+y
# print(r(11,12));

# z=lambda x,y : x if x>y else y
# print(z(12,15));
# print(z(int(input("Enter first number: ")), int(input("Enter second number: "))));


# ! factorial of number using lambda expression
r=lambda n: 1 if n==1 else n*r(n-1)
print("Factorial of a number",r(int(input("Enter a number: "))))
