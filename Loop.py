
# ! for loop
for a in "Sangeeta":
    print("Hello", end="  ");


for a in range(5):
    print("Hello", end="  ");

for a in range(291, 300):
    print("Hello",end="  ");

for a in range(1,30,7):
    print("Hello",end="  ");

for a in range(11,3,-2):
    print("Hello", end="  ")

for a in range(11, 3, -2):
    print("Hello", end="  ")
    print("By", end="  ")
    print("hi")


pin=1234
for i in range(3):
    p=int(input("Enter Your Pin:"))
    if p==pin:
        print("Correct Pin")
        print("Transaction successful")
        break
    else:
        print("Incorrect Pin")
else:
    print("Card Blocked");


# ! While loop
x=5
while x<10:
    print("Hello", end=" ")
    x=x+1
