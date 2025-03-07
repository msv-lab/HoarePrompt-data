#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, n is an integer such that 1 <= n <= 500.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: `t` is 0, `sum` is \( n^3 \) for each executed `n`, `i` is `n` + 1, `j` is `n`, `n` must be at least 2 for each execution.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 500`. For each of the `t` test cases, it reads another integer `n` (where `1 <= n <= 500`), calculates a sum based on a specific formula, and prints the sum along with `2 * n`. Additionally, for each value of `n`, it prints two lines of output for each integer from 1 to `n`, where each line contains a fixed pattern of numbers. The function does not return any value. After the function concludes, `t` is 0, and for each executed `n`, the sum is \( n^3 \), `i` is `n + 1`, `j` is `n`, and `n` must be at least 2.

