#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a list of integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: After all iterations, `t` test cases have been processed, and for each test case, either 'Bob' or 'Alice' has been printed based on whether `1` was present in the list `l`. The values of `n`, `l`, `e`, and `m` will reflect the state of the last test case processed. Variables `t` and the list of test cases remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then determines whether the integer `1` is present in the list. If `1` is present, it prints 'Bob'; otherwise, it prints 'Alice'. After processing all test cases, the function concludes without returning any value.

