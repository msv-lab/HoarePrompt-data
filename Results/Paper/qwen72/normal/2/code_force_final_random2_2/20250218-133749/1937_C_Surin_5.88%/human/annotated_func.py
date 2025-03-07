#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 10^4, and p is a permutation of {0, 1, ..., n-1}. The total sum of n across all test cases does not exceed 10^4.
def func():
    I = lambda : list(map(int, input().split(' ')))
    R = lambda : int(input())
    for kp in range(int(input())):
        n = int(input())
        
        g = 0
        
        v1 = 0
        
        for i in range(1, n):
            v2 = i
            print(f'? {v1} {v1} {v2} {v2}')
            sys.stdout.flush()
            r = input('')
            if r == '<':
                v1 = v2
        
        prev = 0
        
        for i in range(1, n):
            print(f'? {v1} {i} {v1} {prev}')
            sys.stdout.flush()
            r = input()
            if r == '>':
                prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: After the loop executes all the iterations, `t` is an integer such that 1 ≤ t ≤ 10^3, `kp` is `t-1`, `n` is greater than 1 for each test case, `g` is 0, `v1` is `n-1` for the last test case, `i` is `n-1` for the last test case, `v2` is `n-1` for the last test case, `r` is the final user input for the last test case, `prev` is the last index where `r` was '>', or 0 if `r` was never '>' for the last test case. The `sys.stdout.flush()` function has been called for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by an integer `n` and implicitly a permutation `p` of the set {0, 1, ..., n-1}. For each test case, it queries the relative order of elements in the permutation through a series of interactive questions and outputs two indices that represent a specific relationship within the permutation. After processing all test cases, the function ensures that the output for each test case is flushed to the standard output. The final state of the program includes the completion of all test cases, with the last processed values of `n`, `v1`, `i`, `v2`, `r`, and `prev` reflecting the state of the last test case.

