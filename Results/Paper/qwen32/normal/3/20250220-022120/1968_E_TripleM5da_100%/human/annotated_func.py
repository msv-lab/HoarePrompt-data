#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: t is an integer such that 1 <= t <= 50, n is the integer value provided by the user input for the last test case, i is n + 1.
#Overall this is what the function does:The function processes `t` test cases, where each test case involves an integer `n` (with 2 <= n <= 10^3). For each test case, it outputs a series of pairs of integers, starting with (1, 1) and (1, 2), followed by pairs (i, i) for each integer `i` from 3 to `n`.

