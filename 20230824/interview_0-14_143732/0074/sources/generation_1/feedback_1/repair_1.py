def is_prime(x):
    if x <= 1:
        return False
    for i in range(3, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())

if is_prime(n):
    print(1)
    print(n)
else:
    if is_prime(n - 3):
        print(2)
        print(3, n - 3)
    else:
        for p in range(3, n - 2, 2):
            if is_prime(p) and is_prime(n - p):
                print(3)
                print(p, n - p)
                break
        else:  # No solution found
            print("No solution found")