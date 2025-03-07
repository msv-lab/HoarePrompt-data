#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, representing the number of piles. Each pile has an integer a_i such that 1 ≤ a_i ≤ 10^9, representing the initial number of stones in the i-th pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is greater than or equal to 0, `tc` is equal to `t`, `n` is an input integer, `a` is a sorted list of integers read from the last input, `maxsize` is the maximum value in the sorted list `a`, `mexsize` is the smallest positive integer not present in the list `a`. If `mexsize` is greater than `maxsize`, the program follows the logic for the if part. Otherwise, if `mexsize` is less than or equal to `maxsize`, the program follows the logic for the else part.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of piles with a specified number of stones. For each test case, it determines the smallest positive integer (mex) not present in the list of stone counts. It then prints 'Alice' or 'Bob' based on whether the mex is even or odd, considering the maximum stone count in the piles. After processing all test cases, the function completes without returning any value.

