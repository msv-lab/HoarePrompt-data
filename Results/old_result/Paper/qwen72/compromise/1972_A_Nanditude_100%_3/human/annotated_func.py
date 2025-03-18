#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, n is an integer such that 1 <= n <= 100, a is a list of n integers sorted in non-decreasing order where 1 <= a_1 <= a_2 <= ... <= a_n <= 10^9, b is a list of n integers sorted in non-decreasing order where 1 <= b_1 <= b_2 <= ... <= b_n <= 10^9.
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
        
    #State: `t` is an input integer such that 1 <= t <= 100, `n` is an input integer and must be greater than 0, `a` is a list of integers provided by the user, `b` is a list of integers provided by the user and sorted in non-decreasing order where 1 <= b_1 <= b_2 <= ... <= b_n <= 10^9, `_` is incremented by `t`, `j` is `n-1` for each iteration of the inner loop, `cnt` is the number of elements in `b` that are less than the first element in `a` that is greater than or equal to the corresponding element in `b` for each test case, and `i` is the index of the first element in `a` that is greater than or equal to the corresponding element in `b` or `n` if all elements in `a` are less than the corresponding elements in `b` for each test case.
#Overall this is what the function does:The function reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads two integers `n` and two lists `a` and `b` of `n` integers each, where both lists are sorted in non-decreasing order. The function then counts the number of elements in `b` that are less than the corresponding element in `a` for each test case and prints this count. After processing all test cases, the function concludes without returning any value.

