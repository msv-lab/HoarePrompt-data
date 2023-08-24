n = int(input("Enter a positive integer n greater or equal to 2: "))
n = abs(n)

if n <= 2:
    print(0)
else:
    print((n - 1) * (n - 1))