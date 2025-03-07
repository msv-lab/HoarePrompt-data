#State of the program right berfore the function call: t is an integer where 1 <= t <= 500, n is an integer where 2 <= n <= 10^5, and a is a list of n integers where 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: `t` is an integer where 1 <= t <= 500, `n` is an input integer where 3 <= n <= 10^5, `a` is a list of integers derived from the input, `i` is `n-3`, `_` is equal to `t`, `max` is the maximum value of the middle element in any sorted sub-list of 3 consecutive elements in `a` for each test case.
#Overall this is what the function does:The function reads multiple test cases from the input. For each test case, it reads an integer `n` and a list `a` of `n` integers. If `n` is 2, it prints the minimum value in the list `a`. Otherwise, it finds the maximum value of the middle element in any sorted sub-list of 3 consecutive elements in `a` and prints this value. After processing all test cases, the function concludes, and the state of the program is that `t` test cases have been processed, each with its respective `n` and `a`, and the appropriate values have been printed for each case.

