#State of the program right berfore the function call: None of the input variables are explicitly defined in the function signature. However, the problem requires the function to interact with an external entity to perform queries and receive responses. The variable n is an integer representing the length of the permutation, and the permutation itself is fixed but unknown. The function must make at most 3n queries to find a pair of indices i and j such that \( p_i \oplus p_j \) is maximized.
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
        
    #State: Output State: The output state consists of two integers, `mak2` and `pans[mak]`, which represent the result of the loop's operations. Specifically, `mak2` is the result of the first part of the loop where the goal is to find a pair of indices `i` and `j` such that \( p_i \oplus p_j \) is maximized. The second part of the loop aims to find the index `pans[mak]` that maximizes the XOR operation with `mak2`. The final output is these two values.
#Overall this is what the function does:The function interacts with an external entity to perform up to 3n queries on a permutation of length n. It first finds an index `mak` that maximizes the bitwise XOR of elements at the same index. Then, it identifies an index `pans[mak]` that maximizes the bitwise XOR with `mak`. Finally, it outputs the values of `mak2` and `pans[mak]` as the result.

