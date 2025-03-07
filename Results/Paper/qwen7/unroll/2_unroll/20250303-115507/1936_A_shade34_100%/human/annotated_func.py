#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem requires interacting with an external entity to determine the permutation \( p \) and find indices \( i \) and \( j \) that maximize \( p_i \oplus p_j \). The interaction involves making at most \( 3n \) queries, where \( n \) is the length of the permutation.
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
        
    #State: Output State: The output state will consist of two numbers separated by a space. The first number represents the index `mak2`, and the second number represents the index `pans[mak]` after executing all iterations of the loop. These indices are determined based on comparisons made between elements of the permutation \( p \) through a series of queries. The exact values depend on the specific permutation \( p \) and the outcomes of the comparisons made during the loop executions.
#Overall this is what the function does:The function interacts with an external entity to determine a permutation \( p \) of length \( n \) and finds indices \( i \) and \( j \) that maximize \( p_i \oplus p_j \). It achieves this by making at most \( 3n \) queries. The function outputs two indices: the first one (\( mak2 \)) is determined early in the process, and the second one (\( pans[mak] \)) is found after comparing multiple elements.

