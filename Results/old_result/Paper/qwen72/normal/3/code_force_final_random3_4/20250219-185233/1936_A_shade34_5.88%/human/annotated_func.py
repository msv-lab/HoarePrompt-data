#State of the program right berfore the function call: The function operates in an interactive environment with a hidden permutation p of integers from 0 to n-1, where n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to compare bitwise OR results of pairs of elements from the permutation. The function must find and output a pair of indices (i, j) such that p_i ⊕ p_j is maximized, and 0 ≤ i, j < n. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop has completed all iterations, `n` is an input integer greater than 0, `mak2` is the index of the element in the permutation that, when used in bitwise OR with any other element, results in the maximum value. `mak` is the index of the element in `pans` that, when used in bitwise OR with `mak2`, also results in the maximum value. `pans` is a list containing all indices `i` for which the bitwise OR of `mak` and `mak2` with `i` and `mak2` is equal, and it must have at least 2 elements. The output buffer has been flushed.
#Overall this is what the function does:The function `func` operates in an interactive environment with a hidden permutation of integers from 0 to n-1, where n is an integer such that 2 ≤ n ≤ 10^4. It makes at most 3n queries to compare bitwise OR results of pairs of elements from the permutation. The function finds and outputs a pair of indices (i, j) such that the bitwise XOR of the elements at these indices is maximized, and 0 ≤ i, j < n. After the function concludes, the output buffer is flushed, and the indices (i, j) are printed. The function does not return any value.

