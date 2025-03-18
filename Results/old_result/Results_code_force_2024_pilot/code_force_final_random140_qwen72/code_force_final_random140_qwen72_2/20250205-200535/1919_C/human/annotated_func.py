#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. Each test case consists of an integer n (1 ≤ n ≤ 2·10^5), followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        lit = list(map(int, input().split()))
        
        a, b = [lit[0]], []
        
        cp = 0
        
        for i in range(1, n):
            if a[-1] < lit[i]:
                b.append(lit[i])
            else:
                a.append(lit[i])
        
        s = 0
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                s += 1
        
        for i in range(1, len(b)):
            if b[i] > b[i - 1]:
                s += 1
        
        print(s)
        
    #State: After all iterations, `t` is a positive integer (1 ≤ t ≤ 10^4), `_` is `t - 1`, `n` is the last input integer, `lit` is the last list of integers read from input, `a` is a list containing the first element of `lit` and any subsequent elements from `lit` that were not appended to `b` because they were not greater than the last element of `a`, `b` is a list containing elements from `lit` that were greater than the last element of `a` at the time of comparison, `s` is the number of times an element in `a` or `b` was greater than its preceding element, `cp` is 0, `i` is `len(b) - 1`, `len(a)` is the final length of `a`.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it takes an integer `n` and a list of `n` integers. It then splits the list into two lists, `a` and `b`, based on whether each element is greater than the last element in `a`. The function calculates the number of times an element in either `a` or `b` is greater than its preceding element and prints this count for each test case. After processing all test cases, the function terminates.

