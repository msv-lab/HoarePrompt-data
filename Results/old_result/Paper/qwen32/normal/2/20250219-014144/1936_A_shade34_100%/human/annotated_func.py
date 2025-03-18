#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³, and for each test case, n is an integer such that 2 ≤ n ≤ 10⁴. The sequence p is a permutation of the set {0, 1, ..., n-1}. The sum of n over all test cases does not exceed 10⁴.
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
        
    #State: `mak2` is the index of the largest element in the permutation `p`, and `pans[mak]` is the index of the smallest element among those with the maximum value in `p`.
#Overall this is what the function does:For each test case consisting of an integer `n` and a permutation `p` of the set {0, 1, ..., n-1}, the function determines and outputs the index of the largest element in the permutation (`mak2`) and the index of the smallest element among those with the maximum value in the permutation (`pans[mak]`).

