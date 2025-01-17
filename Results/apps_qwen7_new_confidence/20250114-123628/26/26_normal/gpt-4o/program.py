def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    k = int(data[1])
    
    # Calculate the maximum number of ones possible
    max_ones = n * (n + 1) // 2
    
    if k > max_ones:
        print(-1)
        return
    
    # Initialize the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix to make it lexicographically maximal and symmetric
    for i in range(n):
        if k <= 0:
            break
        # First, try to fill the diagonal
        matrix[i][i] = 1
        k -= 1
        
        # Then, try to fill the off-diagonal pairs
        for j in range(i + 1, n):
            if k <= 0:
                break
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            else:
                if k == 1:
                    matrix[i][j] = 1
                    k -= 1
    
    # Print the matrix
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
