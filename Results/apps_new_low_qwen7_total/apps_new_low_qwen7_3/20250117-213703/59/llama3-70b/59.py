n = int(input())
a = int(input())
b = int(input())

total_length = 2 * (a * 2 + b)
if total_length <= n:
    print(1)
else:
    print(-(-total_length // n))
