#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, n is an integer such that 2 <= n <= 100, and a is a list of n integers where 1 <= a_i <= 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        kq = 0
        
        for i in range(0, len(a) // 2, 1):
            kq = kq + a[len(a) - i - 1] - a[i]
        
        print(kq)
        
    #State: `t` is an integer such that 1 <= t <= 500, `n` is an integer such that 2 <= n <= 100, `a` is a list of n integers where 1 <= a_i <= 10^9, `ntest` is an input integer. The loop has printed the sum of differences between the largest and smallest elements in the sorted list `a` for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of `n` integers `a`. It then sorts the list `a` and calculates the sum of differences between the largest and smallest elements in the sorted list `a`, for each pair of elements from the start and end of the list, moving towards the center. This sum is printed for each test case. The function does not return any value.

