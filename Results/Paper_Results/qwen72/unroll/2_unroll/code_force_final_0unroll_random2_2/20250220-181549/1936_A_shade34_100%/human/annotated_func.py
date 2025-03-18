#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, n is an integer such that 2 <= n <= 10^4, and p is a permutation of integers from 0 to n-1.
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
        
    #State: After all iterations of the loop, `t` is an integer such that 1 <= t <= 10^3, `n` is the last input integer such that 2 <= n <= 10^4, and `p` remains a permutation of integers from 0 to n-1. The variables `mak`, `mak2`, and `pans` will have been updated based on the inputs and comparisons made during the loop execution, but their exact values depend on the specific inputs and the permutation `p`. Specifically, `mak2` will be the maximum value found in the first part of the loop, and `pans[mak]` will be the maximum value found in the second part of the loop among the elements that are equal to `mak2` in the permutation `p`.
#Overall this is what the function does:The function `func` does not explicitly accept any parameters but interacts with the user through standard input. It performs a series of queries to determine two maximum values in a permutation `p` of integers from 0 to `n-1`, where `n` is an integer provided by the user. For each of `t` test cases (where `1 <= t <= 10^3`), the function identifies the maximum value `mak2` in the permutation and then finds the maximum value among the elements that are equal to `mak2` in the permutation. The function outputs these two values for each test case. After all iterations, `t` remains an integer within its original range, `n` is the last input integer within its range, and `p` remains a permutation of integers from 0 to `n-1`. The variables `mak`, `mak2`, and `pans` are updated during the function's execution, but their exact final values depend on the specific inputs and the permutation `p`.

