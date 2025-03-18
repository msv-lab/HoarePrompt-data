#State of the program right berfore the function call: The function `func` is intended to solve a problem but lacks parameters in its definition. The problem requires an integer `n` (2 ≤ n ≤ 10^3) as input, and the function should output `n` points in an `n x n` grid that maximize the size of the set \(\mathcal{H}\) of distinct Manhattan distances between any pair of cells. The function should be defined with a parameter to accept `n`.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: The loop has executed `t` times, and in each iteration, it has printed `n` lines where each line contains "1 i" for `i` ranging from 1 to `n`. After all iterations, `t` is 0.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `n` (2 ≤ n ≤ 10^3) and prints `n` lines, each containing the pair "1 i" where `i` ranges from 1 to `n`. After processing all `t` test cases, the function completes, and `t` is 0. The function does not return any value.

