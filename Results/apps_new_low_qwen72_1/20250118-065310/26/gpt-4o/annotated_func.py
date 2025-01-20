#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ 10^6.
def func_1():
    input = sys.stdin.read

data = input().strip().split()

n = int(data[0])

k = int(data[1])

max_ones = n * (n + 1) // 2
    if (k > max_ones) :
        print(-1)
        return
        #The program returns nothing, but `-1` has been printed to the console.
    #State of the program after the if block has been executed: *n is the integer value from the input data, k is the integer value from the input data, max_ones is n * (n + 1) // 2, and k is less than or equal to max_ones
    matrix = [([0] * n) for _ in range(n)]
    for i in range(n):
        if k <= 0:
            break
        
        matrix[i][i] = 1
        
        k -= 1
        
        for j in range(i + 1, n):
            if k <= 0:
                break
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            elif k == 1:
                matrix[i][j] = 1
                k -= 1
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 1, `i` is `min(n, k)`, `max_ones` is `n * (n + 1) // 2`, `k` is 0 or negative, `matrix` is an `n` by `n` matrix where for each `i` from 0 to `min(n, k) - 1`, `matrix[i][i]` is 1. For each `i` from 0 to `min(n, k) - 1` and each `j` from `i + 1` to `n - 1`, if `k` was initially greater than or equal to 2, both `matrix[i][j]` and `matrix[j][i]` are set to 1. If `k` was exactly 1, only `matrix[i][j]` is set to 1 for the last `j` where `k` was 1.
    for row in matrix:
        print(' '.join(map(str, row)))
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 1, `i` is `min(n, k)`, `max_ones` is `n * (n + 1) // 2`, `k` is 0 or negative, `matrix` is an `n` by `n` matrix with the same structure as before the loop started.
#Overall this is what the function does:The function reads two integers, `n` and `k`, from standard input, where `1 ≤ n ≤ 100` and `0 ≤ k ≤ 10^6`. It then checks if `k` exceeds the maximum possible number of ones (`max_ones`) in an `n x n` symmetric matrix with a diagonal of ones. If `k` exceeds `max_ones`, the function prints `-1` to the console and exits. Otherwise, it constructs an `n x n` matrix filled with zeros, and fills it with ones in a way that maximizes the number of ones while maintaining symmetry, until `k` is exhausted. Finally, it prints the matrix to the console. After the function concludes, the state of the program includes the values of `n`, `k`, and `max_ones`, and the matrix is printed to the console. The function itself does not return any value.

