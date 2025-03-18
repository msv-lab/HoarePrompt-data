#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem requires interacting with a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \), which is a permutation of \(\{0, 1, \ldots, n-1\}\). The function can ask up to \(3n\) queries of the form "? a b c d" to compare the bitwise OR of pairs of elements in the permutation. After determining the indices \(i\) and \(j\) that maximize \(p_i \oplus p_j\), the function should print "! i j".
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
        
    #State: mak is 3, mak2 is n-1, pans is a list containing [n-2, n-1], num_iterations is 0, i is 3, s is the input string '=', n is the final value after all iterations, and sys.stdout.flush() is executed in each iteration.
#Overall this is what the function does:The function interacts with a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \) by making up to \(3n\) queries of the form "? a b c d" to compare the bitwise OR of pairs of elements in the permutation. After determining the indices \(i\) and \(j\) that maximize \(p_i \oplus p_j\), the function prints "! i j".

