def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def task(x):
    if is_prime(x):
        return x - 1
    for i in range(2, x + 1):
        if x % i == 0:
            return x // i

t = int(input())

for i in range(t):
    x = int(input())
    print(task(x))