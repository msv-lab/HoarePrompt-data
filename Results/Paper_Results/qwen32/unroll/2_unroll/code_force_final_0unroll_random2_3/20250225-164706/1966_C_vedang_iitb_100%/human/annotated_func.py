#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a list of integers a_1, a_2, ..., a_n where 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    t = int(input())
    for tc in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        maxsize = max(a)
        
        a.sort()
        
        mexsize = 1
        
        for sz in a:
            if sz == mexsize:
                mexsize = mexsize + 1
        
        if mexsize > maxsize:
            print('Alice' if mexsize % 2 == 0 else 'Bob')
        else:
            print('Alice' if mexsize % 2 == 1 else 'Bob')
        
    #State: `t` is the number of test cases, `n` is the number of elements in the last test case's list, and `a` is the list of integers from the last test case.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a list of integers. For each test case, it determines the smallest positive integer that is not present in the list (the MEX) and prints 'Alice' if this MEX is even, or 'Bob' if it is odd.

