#State of the program right berfore the function call: Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the matrix a. The number of test cases t (1 ≤ t ≤ 500) is provided first, followed by t test cases. The sum of n^2 over all test cases does not exceed 5 · 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum, r = 0, 0
        
        for i in range(1, n + 1):
            if n * (n + 1) // 2 > i * n:
                r = i
                sum += n * (n + 1) // 2
            else:
                sum += i * n
        
        print(sum, n + r)
        
        for j in range(1, n + r + 1):
            if j <= n:
                print(1, j, end=' ')
                print(*range(1, n + 1))
            else:
                print(2, j % n, end=' ')
                print(*range(1, n + 1))
        
    #State: The output state consists of `t` blocks, where each block contains the sum and `n + r` for that test case, followed by `n + r` lines describing the matrix operations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` representing the size of a matrix. For each test case, it computes a sum based on the value of `n` and prints this sum along with `n + r`, where `r` is derived from the computation. It then prints `n + r` lines describing matrix operations, which involve printing specific row indices and the numbers 1 through `n`.

