#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem requires interacting with a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \), which is a permutation of \(\{0,1,\ldots,n-1\}\). You can ask up to \(3n\) queries of the form "? a b c d" to compare the bitwise OR of pairs of elements in the permutation. After determining the indices \(i\) and \(j\) that maximize \(p_i \oplus p_j\), you must print "! i j".
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
        
    #State: Output State: `i` is equal to the length of `pans`, `mak` is equal to `len(pans) - 1`, `n` is 0 (as it decreases by 1 each iteration and starts as `len(pans) - 1`), `pans` is a list containing all integers from `0` to `len(pans) - 1`, and `sys.stdout.flush()` is executed.
    #
    #After the loop executes all its iterations, `i` will be equal to the length of `pans`, which is `n` (since `pans` contains all integers from `0` to `n-1`). `mak` will be equal to `len(pans) - 1`, which is `n - 1`. The variable `n` will be 0 because it starts as `len(pans) - 1` and decreases by 1 with each iteration until it reaches 0. `pans` will contain all integers from `0` to `n-1`, which is `0` to `n-1` or simply `0` to `len(pans) - 1`. Finally, `sys.stdout.flush()` is called to ensure the output is sent to the standard output.
#Overall this is what the function does:The function interacts with a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \) to find the indices \(i\) and \(j\) that maximize \(p_i \oplus p_j\). It asks up to \(3n\) comparison queries of the form "? a b c d" to determine these indices and then prints "! i j" where \(i\) and \(j\) are the found indices.

