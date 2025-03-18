#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each test case, n is an integer such that 2 <= n <= 10^4, and p is a permutation of the integers from 0 to n-1. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: For each test case, the output is the indices of the largest and second largest elements in the permutation `p`.
#Overall this is what the function does:For each test case, the function determines and outputs the indices of the largest and second largest elements in a given permutation of integers from 0 to n-1.

