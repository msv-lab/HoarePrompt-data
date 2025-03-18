#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, based on the problem description, t (the number of test cases) is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n (the size of the permutation) is an integer such that 2 ≤ n ≤ 10^4. Additionally, the permutation p_0, p_1, ..., p_{n-1} is a permutation of {0, 1, ..., n-1}.
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
        
    #State: Output State: The output state will consist of two integers separated by a space, representing the indices `mak2` and `mak` after all iterations of the loop have finished. These indices are determined based on the comparisons made during the execution of the loop for each test case. Specifically, `mak2` is initially set to the value of `mak` at the end of the first part of the loop, and `mak` is updated through various comparisons within the loop. The final values of `mak2` and `mak` are printed at the end of each test case.
#Overall this is what the function does:The function processes a series of test cases, each involving a permutation of numbers from 0 to n-1. For each test case, it performs a series of comparisons using a specific query format and updates two indices, `mak2` and `mak`. After processing all test cases, it outputs two integers, `mak2` and `mak`, which represent the results of these comparisons.

