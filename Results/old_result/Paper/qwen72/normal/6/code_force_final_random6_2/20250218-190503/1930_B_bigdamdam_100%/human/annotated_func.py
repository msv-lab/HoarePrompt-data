#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 10^5.
def func():
    for i in range(int(input())):
        n = [int(i) for i in input().split()][0]
        
        p = [0] * n
        
        ind = n
        
        for i in range(0, n, 2):
            p[i] = ind
            ind -= 2
        
        ind = 1 + n % 2
        
        for i in range(1, n, 2):
            p[i] = ind
            ind += 2
        
        print(*p)
        
    #State: The loop has completed all iterations. `n` is an integer such that 3 ≤ n ≤ 10^5, and `p` is a list of length `n` where every even-indexed element (starting from 0) is filled with values decreasing by 2 starting from `n` down to `n - (n // 2) * 2`, and every odd-indexed element (starting from 1) is filled with values starting from 1 or 2 (depending on whether `n` is odd or even) and increasing by 2. `ind` is the next even number after the last filled odd index.
#Overall this is what the function does:The function reads an integer from the user, which determines the number of iterations. For each iteration, it reads another integer `n` (where 3 ≤ n ≤ 10^5) and constructs a list `p` of length `n`. The list `p` is filled such that every even-indexed element (starting from 0) contains values decreasing by 2 starting from `n`, and every odd-indexed element (starting from 1) contains values starting from 1 or 2 (depending on whether `n` is odd or even) and increasing by 2. The function then prints the contents of the list `p` for each iteration. After the function concludes, the list `p` is no longer in scope, and the program state is reset for the next iteration, if any.

