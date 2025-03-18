#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. Additionally, the sequence p_0, p_1, ..., p_{n-1} is a permutation of {0, 1, ..., n-1}.
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
        
    #State: The loop has completed all its iterations, and the final output is `! mak2 pans[mak]`.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer \( t \) (number of test cases) and an integer \( n \) (size of the permutation). For each test case, it queries a sequence \( p_0, p_1, \ldots, p_{n-1} \) which is a permutation of \(\{0, 1, \ldots, n-1\}\) using comparison queries. After processing, it outputs two indices: \( mak2 \) and \( pans[mak] \), which represent the result of the comparisons.

