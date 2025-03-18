#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: For each test case, the list `p` is constructed with even indices filled in descending order from `n` and odd indices filled in ascending order starting from `1 + n % 2`.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves an integer `n`. For each test case, it constructs and prints a list `p` of length `n` such that the even indices are filled with descending values starting from `n`, and the odd indices are filled with ascending values starting from `1 + n % 2`.

