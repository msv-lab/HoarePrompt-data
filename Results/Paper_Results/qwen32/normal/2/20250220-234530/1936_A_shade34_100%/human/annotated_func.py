#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³, and for each test case, n is an integer such that 2 ≤ n ≤ 10⁴. The sum of n over all test cases does not exceed 10⁴.
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
        
    #State: `mak2` is the highest index `i` where the response was `'<'` for the last test case, `mak` is the highest index `i` in `pans` (from index 1 to the end) where the response was `'>'` for the last test case, and `pans` contains all indices `i` where the response was `'='` for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each involving a set of indices from 0 to n-1. It interacts with an external system by sending queries and receiving responses to determine specific indices based on comparison results. For each test case, it identifies and outputs two indices: one where a certain condition is met for the last time (`mak2`) and another within a subset of indices (`pans`) where a different condition is met for the last time (`mak`).

