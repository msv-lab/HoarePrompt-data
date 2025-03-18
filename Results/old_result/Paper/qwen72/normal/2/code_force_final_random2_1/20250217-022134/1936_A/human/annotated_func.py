#State of the program right berfore the function call: The function operates in an interactive environment where the input is a secret permutation of integers from 0 to n-1, and the interaction involves querying the comparison of bitwise OR results of selected indices. The function must find a pair of indices (i, j) such that the bitwise XOR of the elements at these indices is maximized, using no more than 3n queries. The number of test cases t satisfies 1 ≤ t ≤ 10^3, and for each test case, the length of the permutation n satisfies 2 ≤ n ≤ 10^4. The total sum of n across all test cases does not exceed 10^4.
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
        
        print('!', mak2, pans[mak])
        
        sys.stdout.flush()
        
    #State: After all iterations, `n` remains the same as the input integer, `i` is `n-1`, `mak` is the index of the last element in `pans` for which the user input was `>`, or 0 if no such input was given, `mak2` is the largest integer `i` (1 ≤ i < n) for which the user input was `<`, `pans` contains all integers `i` (1 ≤ i < n) for which the user input was `=` or `<`, and the standard output buffer has been flushed.
#Overall this is what the function does:The function interacts with an environment to determine a pair of indices (i, j) in a secret permutation of integers from 0 to n-1, such that the bitwise XOR of the elements at these indices is maximized. It achieves this by making a series of queries, ensuring no more than 3n queries are used. For each test case, it outputs the indices (i, j) that maximize the bitwise XOR. After processing all test cases, the function leaves the input variable `n` unchanged, and the standard output buffer is flushed.

