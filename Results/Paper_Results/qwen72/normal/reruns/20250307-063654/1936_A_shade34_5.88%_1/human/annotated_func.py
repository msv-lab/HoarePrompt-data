#State of the program right berfore the function call: The function operates in an interactive environment where the input is a permutation of integers from 0 to n-1, and n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to find a pair of indices (i, j) such that p_i ⊕ p_j is maximized. Each query involves four indices (a, b, c, d) where 0 ≤ a, b, c, d < n. The output of each query is either "<", ">", or "=". The function must terminate immediately if it makes more than 3n queries. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop has completed all iterations, `n` remains unchanged, `mak` is the index of the largest element in `pans` for which the user input was '>', `mak2` is the index of the largest integer `i` (1 ≤ `i` < `n`) for which the user input was '<', and the output buffer has been flushed.
#Overall this is what the function does:The function operates in an interactive environment to find a pair of indices (i, j) in a permutation of integers from 0 to n-1 such that the XOR of the elements at these indices is maximized. It reads the number of test cases and for each test case, it reads an integer n (2 ≤ n ≤ 10^4). The function makes at most 3n queries to the environment, each involving four indices (a, b, c, d) where 0 ≤ a, b, c, d < n, and the environment responds with either "<", ">", or "=". After processing, the function outputs a pair of indices (mak2, mak) where `mak2` is the index of the largest integer `i` (1 ≤ i < n) for which the user input was '<' and `mak` is the index of the largest element in a subset of indices for which the user input was '>'. The function ensures that the output buffer is flushed after each query and after the final output. If the function exceeds 3n queries, it must terminate immediately.

