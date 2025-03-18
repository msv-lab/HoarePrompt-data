#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem requires interacting with a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \), which is a permutation of \(\{0, 1, \ldots, n-1\}\). You can ask up to \(3n\) queries of the form "? a b c d" to compare the bitwise OR of pairs of elements in the permutation.
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
        
    #State: Output State: The output state will consist of two indices, `mak2` and `mak`. `mak2` is the final value of `mak` from the first iteration of the loop, and `mak` is the final value of `mak` from the last iteration of the loop where the final comparison is made among elements in the list `pans`.
    #
    #To understand this, let's break down the loop:
    #
    #1. In the first part of the loop, `mak` is updated based on comparisons between `mak` and other indices from 1 to `n-1`.
    #2. In the second part, `mak2` is initialized to `mak`, and `pans` is populated based on further comparisons involving `mak2` and all indices from 0 to `n-1`.
    #3. In the third part, `mak` is updated based on comparisons within `pans`.
    #4. Finally, the loop prints the pair `(mak2, mak)`.
    #
    #Since the exact permutation \( p_0, p_1, \ldots, p_{n-1} \) is not known, the output state depends on the outcomes of the comparisons made during the loop. However, the final values of `mak2` and `mak` are determined by these comparisons and will be the result of the loop's execution.
#Overall this is what the function does:The function interacts with a hidden permutation of \(\{0, 1, \ldots, n-1\}\) by making up to \(3n\) queries. It first identifies a candidate index `mak` through comparisons, then populates a list `pans` using further comparisons involving `mak2`. Finally, it refines `mak` by comparing elements within `pans` and outputs the pair `(mak2, mak)` as the result.

