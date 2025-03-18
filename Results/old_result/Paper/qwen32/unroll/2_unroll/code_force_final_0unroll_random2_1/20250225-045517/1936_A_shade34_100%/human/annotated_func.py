#State of the program right berfore the function call: The function `func()` does not take any input arguments. It interacts with an external system to receive the number of test cases `t` (where 1 ≤ t ≤ 10^3) and for each test case, it receives an integer `n` (where 2 ≤ n ≤ 10^4) representing the length of a hidden permutation `p` of integers from 0 to n-1. The function can ask up to 3n queries in the form "? a b c d" to compare bitwise OR results of pairs of elements in the permutation, and it must output the indices `i` and `j` that maximize the bitwise XOR of `p_i` and `p_j` in the form "! i j". The sum of `n` over all test cases does not exceed 10^4.
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
        
    #State: The function `func()` has processed all test cases. For each test case, it has determined and printed the indices `i` and `j` that maximize the bitwise XOR of `p_i` and `p_j` in the form "! i j". The state of variables `mak`, `mak2`, `pans`, and `i` within the loop body are reset for each new test case, but the function is ready to process the next test case if there are any. The external system's state regarding the test cases and permutations is unchanged except for the queries made and results received.
#Overall this is what the function does:The function `func()` processes multiple test cases, each involving a hidden permutation of integers from 0 to n-1. For each test case, it interacts with an external system to determine and print the indices `i` and `j` that maximize the bitwise XOR of the elements `p_i` and `p_j` in the permutation. The function uses up to 3n queries to compare bitwise OR results of pairs of elements in the permutation. After processing all test cases, the function does not return any value but outputs the required indices for each test case.

