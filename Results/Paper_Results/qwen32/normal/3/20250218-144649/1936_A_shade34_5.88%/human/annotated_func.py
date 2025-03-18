#State of the program right berfore the function call: The function `func()` does not take any input arguments directly. Instead, it interacts with the judge through input and output operations. The interaction starts with reading the number of test cases `t` (1 ≤ t ≤ 10^3). For each test case, it reads an integer `n` (2 ≤ n ≤ 10^4) representing the length of the secret permutation `p`. The function can then perform up to 3n queries of the form "? a b c d" (0 ≤ a, b, c, d < n) to compare the bitwise OR of pairs of elements in `p`. After determining the indices `i` and `j` such that `p_i ⊕ p_j` is maximized, the function outputs "! i j". The sum of `n` over all test cases does not exceed 10^4.
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
        
    #State: t is 0, n is the input integer from the last test case, mak2 is the index of the element that maximizes the bitwise XOR with another element in the last test case, mak is the index of the element that, when XORed with the element at mak2, gives the maximum value, and pans is a list of all indices i for which the input was '=' or the last index i for which the input was '<' in the last test case.
#Overall this is what the function does:The function reads the number of test cases and for each test case, it reads an integer `n` representing the length of a secret permutation `p`. It then performs up to 3n queries to compare the bitwise OR of pairs of elements in `p`. After determining the indices `i` and `j` that maximize the bitwise XOR of `p_i` and `p_j`, it outputs "! i j".

