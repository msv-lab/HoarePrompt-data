n = int(input())

# Read the matrix and convert hexadecimal numbers to their binary representations
matrix = []
for _ in range(n):
    row = input().strip()
    binary_row = bin(int(row, 16))[2:].zfill(n)
    matrix.append(binary_row)

# Initialize the maximum x
max_x = 1

# Iterate over all possible values of x
for x in range(2, n + 1):
    # Check if x is a divisor of n
    if n % x == 0:
        # Check if an x-compression is possible
        possible = True
        for i in range(0, n, x):
            for j in range(0, n, x):
                # Check if all elements in the x-compression are the same
                element = matrix[i][j]
                for a in range(i, i + x):
                    for b in range(j, j + x):
                        if matrix[a][b] != element:
                            possible = False
                            break
                    if not possible:
                        break
                if not possible:
                    break
            if not possible:
                break
        # Update the maximum x if an x-compression is possible
        if possible:
            max_x = x
        else:
            break

# Print the maximum x
print(max_x)