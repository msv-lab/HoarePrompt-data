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
        
    #State: `t` is 0, `_` is a placeholder (no specific value required), `n` is the last input integer, `a` is the last list of `n` integers sorted in non-decreasing order with 1 <= a_1 <= a_2 <= ... <= a_n <= 10^9, `b` is the last list of `n` integers sorted in non-decreasing order with 1 <= b_1 <= b_2 <= ... <= b_n <= 10^9, `i` is the number of elements in `a` that are less than or equal to the corresponding elements in `b` up to the last element of `b`, `j` is `n-1`, and `cnt` is the number of elements in `b` that are less than the first element in `a` up to the last element of `b`.
#Overall this is what the function does:The function reads a positive integer `t` (1 <= t <= 100) indicating the number of test cases. For each test case, it reads a positive integer `n` (1 <= n <= 100) and two lists `a` and `b` of `n` integers each, both sorted in non-decreasing order (1 <= a_1 <= a_2 <= ... <= a_n <= 10^9 and 1 <= b_1 <= b_2 <= ... <= b_n <= 10^9). The function then calculates and prints the number of elements in `b` that are less than the corresponding elements in `a`. After processing all test cases, the function concludes with `t` being 0, and the last processed values of `n`, `a`, and `b` remaining as they were at the end of the last test case.

