#State of the program right berfore the function call: The function `func()` does not take any input arguments. It interacts with an external system to receive the number of test cases `t` (1 ≤ t ≤ 10^3), and for each test case, it receives an integer `n` (2 ≤ n ≤ 10^4) representing the length of a hidden permutation `p_0, p_1, ..., p_{n-1}` of the set `{0, 1, ..., n-1}`. The function can ask up to 3n queries of the form "? a b c d" (0 ≤ a, b, c, d < n) to compare the bitwise OR of two pairs of elements from the permutation, and it must output the indices `i` and `j` (0 ≤ i, j < n) that maximize the bitwise XOR `p_i ⊕ p_j` for each test case.
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
        
    #State: The function `func()` has processed all test cases. For each test case, it has determined and output the indices `i` and `j` that maximize the bitwise XOR `p_i ⊕ p_j`. The function has used a series of queries to compare the bitwise OR of different pairs of elements in the hidden permutation to identify these indices. The state of variables `mak`, `mak2`, and `pans` is specific to the current test case and resets for each new test case. The external system has been queried up to 3n times per test case as required.
#Overall this is what the function does:The function `func()` processes multiple test cases, each involving a hidden permutation of integers from 0 to n-1. For each test case, it determines and outputs the indices `i` and `j` that maximize the bitwise XOR of the elements at these indices. The function interacts with an external system to receive the number of test cases and the length of each permutation, and it queries up to 3n times per test case to compare the bitwise OR of different pairs of elements in the permutation.

