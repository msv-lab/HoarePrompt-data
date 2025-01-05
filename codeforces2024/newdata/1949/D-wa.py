import sys
import math

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    matrix = [list(line) for line in data[1:n+1]]
    
    # Calculate the maximum allowed consecutive videos of the same type
    max_consecutive = math.ceil(3 * n / 4)
    
    # Fill the matrix
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == '?':
                # We can choose either 'F' or 'S', let's alternate
                # Count the current number of 'F' and 'S' in the row
                f_count = sum(1 for k in range(n) if matrix[i][k] == 'F')
                s_count = sum(1 for k in range(n) if matrix[i][k] == 'S')
                
                # Choose the one that keeps the balance
                if f_count <= s_count:
                    matrix[i][j] = 'F'
                    matrix[j][i] = 'F'
                else:
                    matrix[i][j] = 'S'
                    matrix[j][i] = 'S'
    
    # Output the result
    for line in matrix:
        print(''.join(line))

if __name__ == "__main__":
    main()