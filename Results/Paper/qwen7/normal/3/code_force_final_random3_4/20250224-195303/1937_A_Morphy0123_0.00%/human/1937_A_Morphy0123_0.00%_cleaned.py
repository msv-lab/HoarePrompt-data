n_cases = int(input())
for i in range(n_cases):
    n = int(input())
    if n == 1:
        print(1)
    else:
        power = 1
        while power < log2(n):
            power += 1
        if power == n:
            print(2 ** power)
        else:
            power -= 1
            print(2 ** power)