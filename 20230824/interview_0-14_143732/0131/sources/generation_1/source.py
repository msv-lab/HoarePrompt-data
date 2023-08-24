def check_stones(n, x, y):
    for i in range(n):
        if x[i] > y[i]:
            return "No"
        elif i > 0 and x[i] < x[i-1]:
            return "No"
        elif i < n-1 and x[i] > x[i+1]:
            return "No"
    return "Yes"

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(check_stones(n, x, y))