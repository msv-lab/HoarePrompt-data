#State of the program right berfore the function call: The function `func` does not take any input parameters, but it is expected to handle multiple test cases. Each test case involves an integer `n` (2 ≤ n ≤ 10^3), representing the size of an n x n grid. The function should internally process a series of such test cases, where the number of test cases `t` is a positive integer (1 ≤ t ≤ 50).
def func():
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: `t` is 0, `n` is the last input integer (2 ≤ n ≤ 10^3), and `i` is `n`.
#Overall this is what the function does:The function `func` processes a series of test cases, where the number of test cases `t` is a positive integer (1 ≤ t ≤ 50). For each test case, it reads an integer `n` (2 ≤ n ≤ 10^3) representing the size of an n x n grid. The function then prints a series of lines, each containing the number `1` followed by a space and the integer `i` (where `i` ranges from 1 to `n`). After processing all test cases, the function ends with `t` being 0, `n` being the last input integer (2 ≤ n ≤ 10^3), and `i` being `n`. The function does not return any value.

