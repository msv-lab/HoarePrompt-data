#State of the program right berfore the function call: The function operates within a test case environment where the input is a sequence p of integers, which is a permutation of {0, 1, ..., n-1}, and n is an integer such that 2 ≤ n ≤ 10^4. The function can interactively query the comparison of bitwise OR results between pairs of elements from the sequence p, and must find a pair of indices (i, j) such that p_i ⊕ p_j is maximized, using at most 3n queries.
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
        
    #State: The loop will output the indices (mak2, mak) such that the bitwise OR of the elements at these indices in the permutation p is maximized. The variables `mak2` and `mak` will hold the indices of the elements that achieve this maximum bitwise OR value.
#Overall this is what the function does:The function operates within a test case environment where it receives a sequence `p` of integers, which is a permutation of {0, 1, ..., n-1}, and an integer `n` (2 ≤ n ≤ 10^4). It interactively queries the comparison of bitwise OR results between pairs of elements from the sequence `p` and finds a pair of indices (i, j) such that the bitwise OR of `p_i` and `p_j` is maximized. The function outputs these indices (i, j) after performing at most 3n queries.

