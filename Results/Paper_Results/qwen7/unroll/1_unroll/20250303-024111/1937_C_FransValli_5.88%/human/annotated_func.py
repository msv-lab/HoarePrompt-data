#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. Additionally, p is a permutation of integers from 0 to n-1, but its exact values are unknown until queried.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. After executing the loop, k is the integer that minimizes the value of the expression `|k - i|` for all `i` from 1 to n-1, and best is the integer that minimizes the value of the expression `|best - i|` for all `i` from 1 to n-1, with the constraints that `k` and `best` are determined through the given queries.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer \( n \) and implicitly a permutation \( p \). For each test case, it determines two integers \( k \) and \( best \) by querying the relative positions of elements in the permutation. Specifically, \( k \) is chosen to minimize the sum of absolute differences \( |k - i| \) for all \( i \) from 1 to \( n-1 \), and \( best \) is chosen similarly but relative to \( k \). Finally, it outputs the values of \( k \) and \( best \) for each test case.

