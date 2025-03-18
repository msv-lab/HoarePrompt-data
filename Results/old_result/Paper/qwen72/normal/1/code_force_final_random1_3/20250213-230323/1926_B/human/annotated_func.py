#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 10, representing the size of the grid. Each grid is represented by a list of n strings, each string containing n characters ('0' or '1'). The grid contains exactly one triangle or one square that includes all the '1's, and the shape cannot consist of exactly one '1'.
def func():
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print('SQUARE')
        else:
            print('TRIANGLE')
        
    #State: The loop counter `i` is equal to `a`, indicating that the loop has completed all its iterations. The variable `k` is a list that may contain multiple counts of '1's from each input string `b` that contained at least one '1' during the iterations. The variable `t` remains an integer where 1 ≤ t ≤ 100, `n` remains an integer where 2 ≤ n ≤ 10, and the grid remains a list of `n` strings, each string containing `n` characters ('0' or '1'). The grid still contains exactly one triangle or one square that includes all the '1's, and the shape cannot consist of exactly one '1'. The variable `a` is now 0, as it has been decremented by the loop.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads another integer `n` and a grid of `n` x `n` characters ('0' or '1'). It then determines and prints whether the shape formed by the '1's in the grid is a 'SQUARE' or a 'TRIANGLE'. After processing all test cases, the function completes, and the program state is such that all input has been processed and the appropriate shape for each test case has been printed. The original values of `t` and `n` remain unchanged, and the grid retains its initial configuration.

