#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: `t` is an integer such that 1 <= t <= 50, and for each of the `t` test cases, `n` is an integer such that 2 <= n <= 10^3, `i` is `n`.
#Overall this is what the function does:The function `func` processes a series of test cases, where the number of test cases `t` is an integer between 1 and 50. For each test case, it reads an integer `n` between 2 and 10^3. The function then prints a series of pairs of integers: (1, 1), (1, 2), and for each integer `i` from 3 to `n` inclusive, it prints (i, i). The function does not return any value, but it affects the program state by consuming input and producing output for each test case. After the function concludes, the input values `t` and `n` for each test case are processed, and the corresponding pairs are printed to the console.

