def check_stones(n, x, y):
    for i in range(n):
        if abs(x[i] - y[i]) > 1:
            return "No"
    return "Yes"

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(check_stones(n, x, y))