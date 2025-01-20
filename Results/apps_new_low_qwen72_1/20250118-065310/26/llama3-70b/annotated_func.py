#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and k is an integer such that 0 ≤ k ≤ 10^6.
def func():
    n, k = map(int, input().split())
    if (k > n * (n + 1) // 2) :
        print(-1)

exit()
    #State of the program after the if block has been executed: *`n` and `k` are integers provided by the user, such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ 10^6. If `k` > `n * (n + 1) // 2`, the condition holds true, indicating that `k` is greater than the sum of the first `n` natural numbers.
    matrix = [([0] * n) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if k > 0:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 100, `k` is an integer such that 0 ≤ k ≤ max(0, k - (n * (n + 1) // 2)), and `matrix` is a `n` x `n` matrix where the lower triangle and diagonal elements are set to 1 up to the first `min(k, n * (n + 1) // 2)` pairs.
    for row in matrix:
        print(' '.join(map(str, row)))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 100, `k` is an integer such that 0 ≤ k ≤ max(0, k - (n * (n + 1) // 2)), `matrix` is a `n` x `n` matrix where the lower triangle and diagonal elements are set to 1 up to the first `min(k, n * (n + 1) // 2)` pairs, `row` is the last row of the matrix.
#Overall this is what the function does:The function `func` reads two integers, `n` and `k`, from the user input. It checks if `k` is greater than the sum of the first `n` natural numbers (`n * (n + 1) // 2`). If `k` exceeds this sum, the function prints `-1` and exits. Otherwise, it initializes an `n x n` matrix filled with zeros. The function then sets the lower triangular and diagonal elements of the matrix to `1` until `k` becomes zero or the matrix is fully populated. Finally, the function prints each row of the matrix. After the function concludes, `n` remains an integer such that 1 ≤ n ≤ 100, `k` is reduced to the maximum of 0 and the original `k` minus the number of `1`s placed in the matrix, and the `n x n` matrix has its lower triangular and diagonal elements set to `1` up to the first `min(k, n * (n + 1) // 2)` pairs. If `k` was initially too large, the function prints `-1` and exits early.

