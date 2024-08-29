
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. +\n2. -\n3. *\n4. /")
choice = int(input("Enter the onperation you want to perform: "))


if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
elif choice == 4:
    print(a/b)
else:
    print("Invalid choice")
    