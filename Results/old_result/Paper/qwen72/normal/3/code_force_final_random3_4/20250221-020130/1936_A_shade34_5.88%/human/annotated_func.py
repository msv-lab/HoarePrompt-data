#State of the program right berfore the function call: The function operates in an interactive environment where the input is provided through queries and responses. The sequence p is a permutation of {0, 1, ..., n-1}, and n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to find indices i and j (0 ≤ i, j < n) that maximize p_i ⊕ p_j.
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
        
    #State: The loop will have executed the specified number of iterations, and for each iteration, it will have printed the indices `mak2` and `mak` that maximize the XOR operation `p_i ⊕ p_j` for the given permutation `p`. The variables `mak`, `mak2`, and `pans` will have been updated during each iteration to reflect the indices and values found, but their final values will depend on the specific permutation `p` and the input provided during the interactive queries.
#Overall this is what the function does:The function operates in an interactive environment to find and print two indices `mak2` and `mak` from a permutation `p` of the set {0, 1, ..., n-1} that maximize the bitwise XOR operation `p_i ⊕ p_j`, where `n` is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to achieve this. For each provided permutation, the function updates and uses internal variables to determine the indices and prints them in the format `! mak2 mak`. The function repeats this process for the number of test cases specified by the initial input.

