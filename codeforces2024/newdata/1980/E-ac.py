def main():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # Read the matrix dimensions n x m
        ab = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(2)]  # Initialize a 3D list for matrices a and b
        
        # Read matrix a and b
        for x in range(2):
            for i in range(1, n + 1):
                row = list(map(int, input().split()))
                for j in range(1, m + 1):
                    ab[x][i][j] = row[j - 1]
        
        # Initialize the sum array
        sum_array = [[[0, 0] for _ in range(n * m + 5)] for _ in range(2)]

        # Compute the row and column sums for both matrices
        for x in range(2):
            # Calculate row sums
            for i in range(1, n + 1):
                row_sum = sum(ab[x][i][j] for j in range(1, m + 1))
                for j in range(1, m + 1):
                    sum_array[x][ab[x][i][j]][0] = row_sum

            # Calculate column sums
            for j in range(1, m + 1):
                col_sum = sum(ab[x][i][j] for i in range(1, n + 1))
                for i in range(1, n + 1):
                    sum_array[x][ab[x][i][j]][1] = col_sum

        # Check if the row and column sums match
        ok = True
        for i in range(1, n * m + 1):
            if sum_array[0][i][0] != sum_array[1][i][0] or sum_array[0][i][1] != sum_array[1][i][1]:
                ok = False
                break

        # Output the result
        if ok:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()