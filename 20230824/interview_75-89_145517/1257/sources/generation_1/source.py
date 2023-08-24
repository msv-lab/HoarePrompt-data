n, k = map(int, input().split())

# calculate the maximum possible sum in the k-th column
max_sum = n*n - (n-k)*n

# initialize the table with all zeros
table = [[0 for _ in range(n)] for _ in range(n)]

# fill the table in increasing order
num = 1
for i in range(n):
    for j in range(n):
        table[i][j] = num
        num += 1

# swap the elements in the k-th column to maximize the sum
for i in range(n):
    if table[i][k-1] != n*n:
        table[i][k-1], table[i][n-1] = table[i][n-1], table[i][k-1]
        break

# print the maximum possible sum
print(max_sum)

# print the table
for i in range(n):
    print(" ".join(str(x) for x in table[i]))