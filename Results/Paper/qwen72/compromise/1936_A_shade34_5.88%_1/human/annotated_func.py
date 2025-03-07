#State of the program right berfore the function call: The function operates in an interactive environment where the input is a sequence of queries and responses. The sequence p_0, p_1, ..., p_{n-1} is a permutation of {0, 1, ..., n-1} for each test case, and n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries of the form "? a b c d" where 0 ≤ a, b, c, d < n, and the response to each query is one of "<", ">", or "=". The function must output a pair of indices i and j (0 ≤ i, j < n) such that p_i ⊕ p_j is maximized. The total number of test cases t is an integer such that 1 ≤ t ≤ 10^3, and the sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop has completed all iterations for each test case. `mak` is the index of the last element in `pans` that maximized the response to the query, `mak2` is the index of the permutation element that was found to be the maximum in the first loop, `pans` is a list containing all indices for which the user input was `=` or `<` during the loop execution, and the output buffer has been flushed after each query and final output.
#Overall this is what the function does:The function operates in an interactive environment where it processes a series of test cases. For each test case, it reads an integer `n` and then interacts with the environment by making queries to find a pair of indices `(i, j)` such that the XOR of the elements at these indices in a permutation of integers from 0 to `n-1` is maximized. The function outputs this pair of indices for each test case. After processing all test cases, the function ensures that the output buffer is flushed.

