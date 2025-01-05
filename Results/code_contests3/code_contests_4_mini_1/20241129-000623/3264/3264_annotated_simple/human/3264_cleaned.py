n = int(raw_input())
if n <= 2:
    print - 1
elif n & 1:
    (print(n * n - 1) / 2, (n * n + 1) / 2)
else:
    (print(n * n / 4 - 1), n * n / 4 + 1)