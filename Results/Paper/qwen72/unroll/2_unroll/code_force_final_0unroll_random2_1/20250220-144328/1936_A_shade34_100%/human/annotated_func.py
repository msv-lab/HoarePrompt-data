#State of the program right berfore the function call: The function `func` is designed to interact with a hidden permutation `p` of integers from 0 to n-1, where `n` is a non-negative integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to find a pair of indices (i, j) such that the bitwise XOR of `p_i` and `p_j` is maximized. Each query involves selecting four indices (a, b, c, d) within the range 0 ≤ a, b, c, d < n, and receiving a comparison result between `(p_a | p_b)` and `(p_c | p_d)`. The function must handle multiple test cases, with the total sum of `n` across all test cases not exceeding 10^4.
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
        
    #State: The loop has finished executing for all test cases. For each test case, the function has determined a pair of indices (mak2, pans[mak]) such that the bitwise XOR of `p[mak2]` and `p[pans[mak]]` is maximized, and has printed this pair. The variables `mak`, `mak2`, and `pans` are reset for each test case, and the loop iterates over all provided test cases.
#Overall this is what the function does:The function `func` interacts with a hidden permutation of integers from 0 to n-1, where n is a non-negative integer (2 ≤ n ≤ 10^4). For each test case, it determines a pair of indices (mak2, pans[mak]) such that the bitwise XOR of the elements at these indices in the permutation is maximized. The function prints this pair for each test case and handles multiple test cases, with the total sum of n not exceeding 10^4. After processing all test cases, the function concludes, and the final state is that the pairs of indices have been printed for each test case.

