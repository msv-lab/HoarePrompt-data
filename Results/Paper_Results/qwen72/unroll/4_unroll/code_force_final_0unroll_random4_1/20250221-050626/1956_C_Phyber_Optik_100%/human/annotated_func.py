#State of the program right berfore the function call: The function does not take any input parameters, but it is expected to handle multiple test cases. Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the matrix. The number of test cases t (1 ≤ t ≤ 500) is provided in the input, and the sum of n^2 over all test cases does not exceed 5 \cdot 10^5.
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
        
    #State: The loop has finished executing all iterations. For each test case, the final value of `sum` is calculated as the sum of the series (i * i - (i - 1) * (i - 1)) * i for i from 2 to n, and the value of `n + n` is printed alongside it. Additionally, for each value of `j` from 1 to n, two lines are printed: the first line contains `1, n - j + 1,` followed by the numbers from 1 to n, and the second line contains `2, n - j + 1,` followed by the numbers from 1 to n. The loop variable `_` has been iterated from 0 to t-1, and the loop variable `i` has been iterated from 2 to n for each test case. The loop variable `j` has been iterated from 1 to n for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `n` (1 ≤ n ≤ 500) representing the size of a matrix. The function calculates a sum based on the series (i * i - (i - 1) * (i - 1)) * i for i from 2 to n, and prints this sum alongside `n + n`. Additionally, for each value of `j` from 1 to n, it prints two lines: the first line contains `1, n - j + 1,` followed by the numbers from 1 to n, and the second line contains `2, n - j + 1,` followed by the numbers from 1 to n. After processing all test cases, the function concludes.

