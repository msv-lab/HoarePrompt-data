#State of the program right berfore the function call: The function `func()` does not take any input parameters directly. Instead, it interacts with an external system to receive the number of test cases `t` (1 ≤ t ≤ 10^3), and for each test case, it receives an integer `n` (2 ≤ n ≤ 10^4) followed by a hidden permutation `p_0, p_1, ..., p_{n-1}` of the integers from 0 to n-1. The function can make queries to the system by printing lines in the format "? a b c d" where 0 ≤ a, b, c, d < n, and it will receive a response of "<", "=", or ">" based on the comparison of the bitwise OR operations on the elements of the permutation. The function must find two indices i and j such that `p_i ⊕ p_j` is maximized and print the result in the format "! i j" without exceeding 3n queries per test case. The sum of n over all test cases does not exceed 10^4.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        mak = 0
        
        for i in range(1, n):
            print('?', mak, mak, i, i)
            sys.stdout.flush()
            if str(input()) == '<':
                mak = i
        
        mak2 = mak
        
        pans = []
        
        for i in range(n):
            print('?', mak, mak2, i, mak2)
            sys.stdout.flush()
            s = str(input())
            if s == '<':
                mak = i
                pans = [i]
            elif s == '=':
                pans.append(i)
        
        mak = 0
        
        for i in range(1, len(pans)):
            print('?', pans[mak], pans[mak], pans[i], pans[i])
            sys.stdout.flush()
            if str(input()) == '>':
                mak = i
        
        print('!', mak2, mak)
        
        sys.stdout.flush()
        
    #State: `t` test cases have been processed, each with an integer `n` and a hidden permutation `p`. For each test case, the function has found and printed two indices `i` and `j` such that `p_i ⊕ p_j` is maximized. The variables `mak`, `mak2`, `pans`, and `i` are in a state as they were after the last iteration of the inner loops for the final test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each involving a hidden permutation of integers from 0 to n-1. For each test case, it interacts with an external system to determine two indices `i` and `j` that maximize the bitwise XOR (`p_i ⊕ p_j`) of the permutation elements. The function outputs these indices in the format "! i j" without exceeding 3n queries per test case.

