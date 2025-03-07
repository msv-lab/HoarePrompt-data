#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n² over all test cases does not exceed 5 × 10⁵.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 500, and `n` is an integer such that 1 ≤ n ≤ 500. For each iteration of the loop, the following operations are performed:
    #
    #1. A new value of `n` is taken as input.
    #2. A variable `sum` is initialized to 1.
    #3. A nested loop calculates `sum` using the formula `(i * i - (i - 1) * (i - 1)) * i` for `i` ranging from 2 to `n`.
    #4. The result of `sum` and `n + n` are printed.
    #5. Another nested loop prints two lines for each value of `j` from 1 to `n`, with the first line containing `1`, `n - j + 1`, and a range of numbers from 1 to `n`, and the second line containing `2`, `n - j + 1`, and the same range of numbers from 1 to `n`.
    #
    #After all iterations of the loop, the final values of `t` and `n` will be the last values provided as input within the loop. The output will consist of multiple lines, each corresponding to an iteration of the loop, showing the calculated `sum` and `n + n`, followed by two lines of printed ranges for each value of `j`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` (1 ≤ t ≤ 500) and an integer `n` (1 ≤ n ≤ 500). For each test case, it calculates a sum based on the formula `(i * i - (i - 1) * (i - 1)) * i` for `i` ranging from 2 to `n`. It then prints the calculated sum and `n + n`. Additionally, it prints two lines for each value of `j` from 1 to `n`, with the first line containing `1`, `n - j + 1`, and a range of numbers from 1 to `n`, and the second line containing `2`, `n - j + 1`, and the same range of numbers from 1 to `n`. After processing all test cases, the function outputs multiple lines of results corresponding to each test case.

