#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. The sequence p_0, p_1, ..., p_{n-1} is a permutation of {0, 1, ..., n-1}. The interaction involves asking queries in the form "? a b c d" where 0 ≤ a, b, c, d < n, and receiving a response of "<", "=", or ">" based on the comparison of (p_a | p_b) and (p_c | p_d). The goal is to find indices i and j such that p_i ⊕ p_j is maximized using at most 3n queries. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: `mak` is the index in `pans` for which `p[i] ⊕ p[mak2]` is maximized, `mak2` is the index of the element in the permutation that has the maximum bitwise OR with all other elements, `pans` is a list of indices that have the same bitwise OR result with `mak2` as the maximum, and `n` remains unchanged.
#Overall this is what the function does:The function determines and returns indices `i` and `j` such that the bitwise XOR of the elements at these indices in a hidden permutation sequence is maximized, using at most 3n queries per test case.

