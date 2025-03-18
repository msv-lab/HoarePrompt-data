#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, n is a positive integer such that 1 <= n <= 100, a is a list of n integers sorted in non-decreasing order with 1 <= a_1 <= a_2 <= ... <= a_n <= 10^9, b is a list of n integers sorted in non-decreasing order with 1 <= b_1 <= b_2 <= ... <= b_n <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        cnt = 0
        
        i = 0
        
        for j in range(n):
            if b[j] < a[i]:
                cnt += 1
            else:
                i += 1
        
        print(cnt)
        
    #State: `t` is 0, `_` is `t-1`, `n` is an input integer, `a` is a list of integers input by the user, `b` is a list of integers input by the user, `cnt` is the number of elements in `b` that are less than `a[i]` for each `j` from 0 to `n-1` for each iteration, `i` is the number of elements in `a` that are less than or equal to the corresponding elements in `b` up to `j = n-1` for each iteration, and `j` is `n-1` for each iteration.
#Overall this is what the function does:The function `func` reads a series of inputs from the user. It first reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n`, followed by two lists of `n` integers each, `a` and `b`, which are sorted in non-decreasing order. The function then counts the number of elements in `b` that are less than the first element in `a` and prints this count for each test case. After processing all test cases, the function concludes, and the state is that `t` is 0, and the counts for each test case have been printed.

