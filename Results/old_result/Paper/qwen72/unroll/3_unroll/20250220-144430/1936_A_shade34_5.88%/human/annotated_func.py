#State of the program right berfore the function call: The function operates in an interactive environment where it receives input and provides output through a series of queries. The input is a permutation p of integers from 0 to n-1, where n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to find two indices i and j (0 ≤ i, j < n) such that p_i ⊕ p_j is maximized. The total sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop will output the indices `mak2` and `mak` such that `p[mak2] ⊕ p[mak]` is maximized for each permutation `p` of integers from 0 to n-1, where `n` is the length of the permutation. The variables `mak`, `mak2`, and `pans` will be reset for each new permutation, and the loop will repeat for the number of test cases specified by the initial input.
#Overall this is what the function does:The function operates in an interactive environment to process multiple test cases, each involving a permutation `p` of integers from 0 to n-1, where `n` is an integer between 2 and 10^4. For each test case, the function queries the environment to find and output two indices `mak2` and `mak` such that the bitwise XOR of `p[mak2]` and `p[mak]` is maximized. The function ensures that it makes at most 3n queries for each permutation. After processing all test cases, the function concludes, and the interactive environment is left in a state where the indices for each permutation have been outputted.

