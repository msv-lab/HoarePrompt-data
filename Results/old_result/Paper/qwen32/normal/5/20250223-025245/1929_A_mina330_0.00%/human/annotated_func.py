#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
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
        
    #State: The loop has executed `ntest` times. For each test case, a sorted list `a` of integers is read, and `kq` is calculated as the sum of the differences between the corresponding elements from the end and the start of the sorted list `a` moving towards the center. After all iterations, `itest` equals `ntest`, and the final `kq` for each test case has been printed.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates the sum of the differences between the largest and smallest elements, the second largest and second smallest elements, and so on, until it reaches the middle of the list. It then prints this sum for each test case.

