#State of the program right berfore the function call: The function should take an integer n as input where 2 <= n <= 10^3, and the input is provided through multiple test cases, each on a new line, with the first line indicating the number of test cases t where 1 <= t <= 50.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: `i` is equal to the input integer `n` for the last test case, and `n` remains unchanged for each test case.
#Overall this is what the function does:The function `func` processes up to 50 test cases, each with an integer `n` where 2 <= n <= 10^3. For each test case, it prints a series of pairs of integers. Specifically, it prints (1, 1), (1, 2), and then for each integer `i` from 3 to `n` (inclusive), it prints (i, i). The function does not return any value; it only prints the output. After the function concludes, the input integer `n` for each test case remains unchanged, and the loop variable `i` is equal to `n + 1` for the last test case.

