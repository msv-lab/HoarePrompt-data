#State of the program right berfore the function call: None of the input variables are explicitly defined in the function signature. However, the problem requires interacting with an external entity to query bitwise operations on a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \), which is a permutation of \(\{0,1,\ldots,n-1\}\). The interaction involves making at most \(3n\) queries to determine the indices \(i\) and \(j\) such that \(p_i \oplus p_j\) is maximized.
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
        
    #State: Output State: mak is 0, mak2 is 0, pans is a list containing the elements from n-1 down to 0, and i is n-1. The variable `s` will be '>' for all comparisons within the loop, and `sys.stdout.flush()` has been executed as necessary during each iteration.
    #
    #This means that after all iterations of the loop have completed, `mak` and `mak2` both end up being 0 because `mak` is reset to 0 at the start of each new iteration of the outer loop. The list `pans` contains the permutation of indices from n-1 down to 0, as it was built up over the iterations without any changes being made to it. The variable `i` is set to n-1, indicating the last index processed in the final iteration.
#Overall this is what the function does:The function interacts with an external entity to determine indices \(i\) and \(j\) such that \(p_i \oplus p_j\) is maximized, where \(p_0, p_1, \ldots, p_{n-1}\) is a permutation of \(\{0,1,\ldots,n-1\}\). It achieves this by making at most \(3n\) queries. After executing the function, it outputs the indices \(i\) and \(j\) that maximize the bitwise XOR operation.

