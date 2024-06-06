a = int(input("Please enter a number for A: "))
b =int(input("Please enter a number for B: "))
c = int(input("Please enter a number for C: "))

if a > b:
    if a > c:
        print(" A is grater Most")
    else:
        print("C is grater Most")
elif b>c:
    print("B is grater Most")
else:
    print("C is grater Most")

