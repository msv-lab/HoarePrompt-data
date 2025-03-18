#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. Additionally, p is a permutation of integers from 0 to n-1, but its exact values are not known beforehand.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. Additionally, p is a permutation of integers from 0 to n-1, and after executing the loop, mak2 and mak are determined based on the comparisons made during the loop iterations.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (1 ≤ t ≤ 10^3) and an integer `n` (2 ≤ n ≤ 10^4). For each test case, it performs a series of comparisons to determine two indices, `mak2` and `mak`. These comparisons involve elements of a permutation `p` of integers from 0 to n-1. After processing all test cases, the function outputs the values of `mak2` and `mak` for each case.

