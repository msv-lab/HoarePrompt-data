#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, n is an integer such that 2 ≤ n ≤ 10^4 for each test case, and the sum of n over all test cases does not exceed 10^4. The sequence p is a permutation of integers from 0 to n-1.
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
        
    #State: _ is t-1, n is the input integer, i is n-1, `mak` is the largest index in `pans` for which the input was '>', `mak2` is the largest index for which the input was '<', `pans` is a list containing all indices for which the input was '=' or the last index for which the input was '<', and the output buffer has been flushed.
#Overall this is what the function does:The function `func` interacts with an external system or user through a series of queries to determine and output two indices, `mak2` and `mak`, from a permutation sequence `p` of integers from 0 to n-1. The function processes `t` test cases, where `t` is an integer between 1 and 10^3, and for each test case, `n` is an integer between 2 and 10^4. The function does not return any value but prints the results of each test case to the standard output. After the function concludes, the output buffer is flushed, and the state of the program includes the processed test cases and the final values of `mak2` and `mak` for each test case.

