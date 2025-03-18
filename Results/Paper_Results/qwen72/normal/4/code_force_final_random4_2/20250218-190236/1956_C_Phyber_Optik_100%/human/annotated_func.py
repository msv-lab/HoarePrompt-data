#State of the program right berfore the function call: The function does not take any input parameters, but it is expected to handle multiple test cases. Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the n×n matrix. The number of test cases t is also an integer (1 ≤ t ≤ 500), and the sum of n^2 over all test cases does not exceed 5 · 10^5.
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
        
    #State: `t` is 0, `sum` is \(1 + \sum_{k=2}^{n} (k^2 - (k-1)^2) \cdot k\) for each test case, `i` is `n + 1` for each test case, `j` is `n` for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 500) and calculates a sum based on a specific formula. It then prints the sum followed by `2n`. Additionally, for each value from 1 to `n`, it prints two lines: the first line starts with `1` followed by `n - j + 1` and a range of numbers from 1 to `n`, and the second line starts with `2` followed by `n - j + 1` and the same range of numbers from 1 to `n`. After processing all test cases, the function terminates with `t` being 0, and the final state for each test case includes the calculated sum and the printed output.

