n, k = map(int, input().split())

# calculate the maximum possible sum in the k-th column
max_sum = (n*n + (n-k)*(k-1)) // k

# initialize the table in increasing order
table = [[0 for _ in range(n)] for _ in range(n)]
num = 1
for i in range(n):
    for j in range(n):
        table[i][j] = num
        num += 1

# find the largest element in the k-th column
max_element = 0
max_row = -1
for i in range(n):
    if table[i][k-1] > max_element:
        max_element = table[i][k-1]
        max_row = i

# swap the largest element to the last position in the k-th column
table[max_row][k-1], table[max_row][n-1] = table[max_row][n-1], table[max_row][k-1]

# print the maximum possible sum
print(max_sum)

# print the table
for row in table:
    print(" ".join(str(x) for x in row))