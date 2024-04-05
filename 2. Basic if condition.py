price = 1000000
int(price)

credit = int(input("Please enter your credit point:\n"))

if 0 < credit < 10:
    print("You need to put down %10")
    print(f"{price * 0.10} Turkish liras" )

else:
    print("You need to put down %20")
    print(f"{price * 0.20} Turkish liras")
