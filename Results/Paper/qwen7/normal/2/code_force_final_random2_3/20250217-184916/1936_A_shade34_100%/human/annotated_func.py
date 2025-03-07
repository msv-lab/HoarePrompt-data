#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. The interactor chooses a fixed permutation p_0, p_1, ..., p_{n-1} which is a permutation of {0, 1, ..., n-1}.
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
        
    #State: mak is n-1, i is n-1, pans is a list containing the integers from 0 to n-1 inclusive, mak2 is n-1, the current value of the input string s is an input from the user (it could be either '<' or '=' for the next iteration if it exists), sys.stdout.flush() has been called 3*n-3 times, and the condition s == '>' is false based on the input received during the last iteration.
#Overall this is what the function does:The function processes a series of test cases where for each case, it interacts with an external entity to determine a specific permutation of numbers from 0 to n-1. It identifies two key elements, `mak` and `mak2`, through a series of queries. After determining these elements, it outputs the final value of `mak2` and the position of `mak` within the permutation. The function performs a total of 3n-3 queries and outputs the results accordingly.

