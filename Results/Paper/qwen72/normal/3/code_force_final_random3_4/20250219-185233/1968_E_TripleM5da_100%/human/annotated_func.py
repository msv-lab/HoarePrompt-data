#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: `t` is an integer such that 1 <= t <= 50, for each of the `t` test cases, `n` is an integer such that 2 <= n <= 10^3, `i` is `t` (the total number of test cases).
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer between 1 and 50. For each test case, it reads an integer `n` such that 2 <= n <= 10^3, and prints a series of pairs of integers. Specifically, it prints (1, 1), (1, 2), and then for each integer `i` from 3 to `n` (inclusive), it prints (i, i). After processing all test cases, the function does not return any value. The final state of the program is that `t` test cases have been processed, and the pairs of integers have been printed for each `n` in the test cases.

