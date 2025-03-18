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
        
    #State: `t` remains unchanged; `ntest` remains unchanged; `n` is the number of elements in the last test case's list; `a` is the sorted list of integers from the last test case; `kq` is the computed value from the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it calculates the sum of differences between the largest and smallest integers, the second largest and second smallest integers, and so on, until the middle of the list is reached. It then prints this sum for each test case.

