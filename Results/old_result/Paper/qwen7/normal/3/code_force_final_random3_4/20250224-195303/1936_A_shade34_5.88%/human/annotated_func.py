#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, based on the problem description, t (the number of test cases) is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n (the size of the permutation) is an integer such that 2 ≤ n ≤ 10^4. Additionally, the permutation p is a list of n integers that is a permutation of {0, 1, ..., n-1}.
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
        
    #State: `mak` is equal to `2n - 1`, `mak2` is `n - 1`, `pans` is a list containing all integers from `n` to `2n - 1` inclusive, and `i` is equal to the length of `pans`, which is `2n - 1`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( n \) and a permutation \( p \) of integers from \( 0 \) to \( n-1 \). For each test case, it queries the relative order of elements in the permutation using a series of comparison operations. After determining the relative order, it outputs two indices: one corresponding to \( 2n - 1 \) and another to \( n - 1 \), effectively providing a summary of the permutation's structure.

