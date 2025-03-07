#State of the program right berfore the function call: The function does not take any input parameters, but it is expected to handle multiple test cases, each with an integer n (1 ≤ n ≤ 500) representing the size of the matrix. The number of test cases t is an integer (1 ≤ t ≤ 500).
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
        
    #State: The loop will execute `t` times, where `t` is the number of test cases. For each test case, the loop will read an integer `n` (1 ≤ n ≤ 500) from the user. After the loop finishes, the variables `sum` and `r` will be calculated and printed for each test case. The variable `sum` will be the sum of either `n * (n + 1) // 2` or `i * n` depending on the condition `n * (n + 1) // 2 > i * n`. The variable `r` will be the last value of `i` that satisfies the condition. Additionally, for each test case, the loop will print a series of lines where the first line is `sum` and `n + r`, followed by `n + r` lines. The first `n` lines will print `1` followed by the line number and the range from 1 to `n`. The remaining lines will print `2` followed by the line number modulo `n` and the range from 1 to `n`.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `t` from the user, representing the number of test cases. For each test case, it reads another integer `n` (1 ≤ n ≤ 500) from the user, representing the size of a matrix. The function calculates and prints two values: `sum` and `n + r`. The variable `sum` is the sum of either `n * (n + 1) // 2` or `i * n` for each integer `i` from 1 to `n`, depending on the condition `n * (n + 1) // 2 > i * n`. The variable `r` is the last value of `i` that satisfies this condition. After printing `sum` and `n + r`, the function prints `n + r` lines. The first `n` lines each start with `1` followed by the line number and the range from 1 to `n`. The remaining lines each start with `2` followed by the line number modulo `n` and the range from 1 to `n`. The function repeats this process for each of the `t` test cases.

