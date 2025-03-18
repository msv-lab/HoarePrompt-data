#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n is an integer such that 3 ≤ n ≤ 10^5. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: For each test case, `p` is a list of `n` elements where the first `floor(n/2)` even indices are filled with values `n, n-2, n-4, ..., n-2*(floor(n/2)-1)` and the odd indices are filled with values `1 + n % 2, 3 + n % 2, 5 + n % 2, ..., n-1 + n % 2`.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`. For each test case, it generates a list `p` of length `n` where the even indices are filled with descending even numbers starting from `n` and the odd indices are filled with ascending odd numbers starting from `1 + n % 2`. The function prints this list for each test case.

