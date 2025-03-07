#State of the program right berfore the function call: The function operates in an interactive environment with a hidden permutation p of integers from 0 to n-1, where 2 ≤ n ≤ 10^4. The function can make at most 3n queries to compare bitwise OR results of selected indices. The goal is to find indices i and j such that p_i ⊕ p_j is maximized.
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
        
    #State: After all iterations of the loop, `i` will be equal to `len(pans) - 1`, `pans` will contain all indices for which the user input was "=" or "<", `mak` will be the index of the last element in `pans` for which the user input was ">", `mak2` will be the largest value of `i` for which the user input was "<" during the loop's execution, and `s` will be the last user input string. The output buffer will have been flushed multiple times during the loop execution, and the output buffer will be flushed again.
#Overall this is what the function does:The function interacts with an environment containing a hidden permutation of integers from 0 to n-1, where 2 ≤ n ≤ 10^4. It aims to find two indices `i` and `j` such that the bitwise XOR of `p[i]` and `p[j]` is maximized. The function achieves this by making at most 3n queries to compare bitwise OR results of selected indices. After the function completes, it outputs the indices `i` and `j` that maximize the bitwise XOR, and the output buffer is flushed.

