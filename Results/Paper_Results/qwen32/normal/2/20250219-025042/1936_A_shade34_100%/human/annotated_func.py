#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. Additionally, there exists a secret permutation p of the set {0, 1, ..., n-1} for each test case.
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
        
    #State: `t` remains unchanged, `n` remains unchanged for each test case, `mak2` is the index of the maximum element in the permutation `p`, `mak` is the index of the maximum element in `pans`, `pans` is a list of indices where the elements are either less than or equal to `mak2`.
#Overall this is what the function does:The function processes multiple test cases, each involving a secret permutation of integers from 0 to n-1. For each test case, it identifies and outputs the index of the maximum element in the permutation and the index of another element that is greater than or equal to this maximum element.

