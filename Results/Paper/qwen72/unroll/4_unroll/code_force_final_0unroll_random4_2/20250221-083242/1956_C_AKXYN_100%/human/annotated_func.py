#State of the program right berfore the function call: The function `func` does not take any input parameters. However, based on the problem description, it is implied that the function will be used in a context where it processes multiple test cases, each with an integer n (1 ≤ n ≤ 500) representing the size of the matrix. The function should be able to handle up to 500 test cases, and the sum of n^2 over all test cases does not exceed 5 \cdot 10^5.
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
        
    #State: The function `func` will have processed all test cases, each with an integer `n` (1 ≤ n ≤ 500) representing the size of the matrix. For each test case, the loop will have printed the result of the formula `res = sum((i + 1) * (2 * i + 1) for i in range(n))` followed by `n << 1` (which is `n * 2`). Additionally, for each `i` from `n` to `1` in descending order, the loop will have printed two lines: '1 i' followed by the numbers from 1 to `n`, and '2 i' followed by the numbers from 1 to `n`. The loop will have completed all iterations, and the function will be ready to process the next test case or terminate if there are no more test cases.
#Overall this is what the function does:The function `func` processes multiple test cases, each with an integer `n` (1 ≤ n ≤ 500) representing the size of a matrix. For each test case, it prints the result of the formula `res = sum((i + 1) * (2 * i + 1) for i in range(n))` followed by `n * 2`. Additionally, it prints two lines for each integer `i` from `n` down to `1`: the first line is '1 i' followed by the numbers from 1 to `n`, and the second line is '2 i' followed by the numbers from 1 to `n`. After processing all test cases, the function terminates.

