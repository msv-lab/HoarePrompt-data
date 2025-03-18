#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each test case, n is an integer such that 3 <= n <= 10^5. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: For each test case, the list `p` is constructed such that `p[2j] = n - 2j` for even indices `2j < n` and `p[2j+1] = 1 + 4k` for odd indices `2j+1 < n` where `k` is the index of the odd position starting from 0. The value of `t` remains the same.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n`. For each test case, it constructs and prints a list `p` of length `n` such that even-indexed elements are filled in descending order starting from `n`, and odd-indexed elements are filled in ascending order starting from `1` or `2` depending on whether `n` is odd or even.

