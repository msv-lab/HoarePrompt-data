#State of the program right berfore the function call: The function operates in an interactive environment where the input is provided through a series of queries. The sequence p is a permutation of {0, 1, ..., n-1}, and n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to find the indices i and j (0 ≤ i, j < n) that maximize p_i ⊕ p_j. The total sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop iterates through a series of inputs, each time updating the variables `mak`, `mak2`, and `pans` to find the indices `i` and `j` that maximize the XOR of the elements in the permutation `p`. After all iterations, the final values of `mak2` and `pans[mak]` are printed as the indices that maximize `p_i ⊕ p_j` for each input permutation. The variables `n` and `mak` are reset for each new input, and `pans` is updated to store the indices that are equal to `mak2` in terms of the XOR comparison.
#Overall this is what the function does:The function operates in an interactive environment to find and print the indices `i` and `j` (0 ≤ i, j < n) that maximize the bitwise XOR of `p_i` and `p_j`, where `p` is a permutation of the set {0, 1, ..., n-1} and `n` is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to find these indices. After processing each input permutation, the function prints the indices `mak2` and `pans[mak]` that maximize `p_i ⊕ p_j`. The function handles multiple test cases, resetting its internal state for each new input.

