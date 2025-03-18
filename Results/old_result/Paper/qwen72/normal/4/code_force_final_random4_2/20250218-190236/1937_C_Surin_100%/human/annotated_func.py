#State of the program right berfore the function call: The function operates in an interactive environment where the input sequence is a permutation of integers from 0 to n-1, and n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to find a pair of indices (i, j) such that the bitwise XOR of p_i and p_j is maximized. The total number of test cases, t, is an integer such that 1 ≤ t ≤ 10^3, and the sum of n over all test cases does not exceed 10^4.
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
            elif r == '=':
                print(f'? {i} {i} {prev} {prev}')
                sys.stdout.flush()
                r2 = input('')
                if r2 == '<':
                    prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: `R` is a lambda function that reads a line of input, converts it to an integer, and returns this integer. `kp` is the number of iterations minus 1, `n` is the final value of `n` for the last iteration, `g` is 0, `v1` is the largest integer `i` for which the input `r` was '<' during the last iteration, `i` is `n-1`, `v2` is `n-1`, `r` is the last input string, `prev` is the last value of `i` for which `r` was '>' or `r` and `r2` were '=' and '<' respectively during the last iteration, and the output buffer has been flushed.
#Overall this is what the function does:The function `func` operates in an interactive environment where it processes multiple test cases. For each test case, it reads an integer `n` representing the length of a permutation of integers from 0 to n-1. The function then makes a series of queries to determine a pair of indices (i, j) such that the bitwise XOR of the elements at these indices in the permutation is maximized. The function outputs the indices (i, j) that achieve this maximum XOR value. After processing all test cases, the function has no return value, but it has printed the results for each test case and flushed the output buffer.

