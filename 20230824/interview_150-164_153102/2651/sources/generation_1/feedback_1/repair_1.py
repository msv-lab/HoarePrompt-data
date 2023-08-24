n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

MOD = 10**9 + 7

# Calculate the differences between consecutive x coordinates
x_diff = [x[i+1] - x[i] for i in range(n-1)]

# Calculate the differences between consecutive y coordinates
y_diff = [y[i+1] - y[i] for i in range(m-1)]

# Calculate the total area by summing the products of width and height
total_area = 0
for width in x_diff:
    for height in y_diff:
        area = width * height
        total_area = (total_area + area) % MOD

# Print the total area modulo 10^9+7
print(total_area)