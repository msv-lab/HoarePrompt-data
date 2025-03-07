#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        mat = [list(range(1, n + 1)) for i in range(n)]
        
        res = 0
        
        for i in range(n):
            res += (i + 1) * (2 * i + 1)
        
        print(res, n << 1)
        
        for i in range(n, 0, -1):
            print('1 %d' % i, *range(1, n + 1))
            print('2 %d' % i, *range(1, n + 1))
        
    #State: Output State: `i` is 0; `n` is 1; `mat` is [[1]]; `res` is 0.
    #
    #Explanation: The loop iterates from `i = n` down to `i = 1`. Given that `n` is initially set to 1, the loop will run only once with `i` starting from 1 and decrementing to 0. During this single iteration, the value of `res` is not modified, so it remains 0. The matrix `mat` is initialized as a list containing a single list `[1]` since `n` is 1. After the loop completes, `i` will be 0, `n` will be 1, `mat` will be `[[1]]`, and `res` will be 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and an integer `n`. For each test case, it initializes a square matrix `mat` of size `n x n` with values ranging from 1 to `n`. It then calculates a result `res` using a specific formula involving `i` and prints this result along with `2 * n`. The function also prints a sequence of commands involving the matrix `mat` for each value of `n` from `n` down to 1. After processing all test cases, the function does not return any value.

