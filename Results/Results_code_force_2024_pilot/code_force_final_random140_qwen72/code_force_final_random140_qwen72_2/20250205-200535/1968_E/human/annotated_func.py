#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 2):
            print(i, i)
        
    #State: `i` is `t`, and `n` remains unchanged for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where 1 <= t <= 50. For each test case, it reads another integer `n` (2 <= n <= 10^3). It then prints a series of pairs of integers. Specifically, it prints (1, 1), (1, 2), and for each integer `i` from 3 to `n + 1`, it prints (i, i). The function does not return any value; it only prints the results to the console. After the function concludes, the input variables `t` and `n` remain unchanged, and the program state reflects the printed output for each test case.

