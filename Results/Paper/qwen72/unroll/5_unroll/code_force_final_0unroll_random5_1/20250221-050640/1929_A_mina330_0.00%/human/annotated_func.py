#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, n is an integer such that 2 <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
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
        
    #State: ntest is an input integer, t is an integer such that 1 <= t <= 500, n is an integer such that 2 <= n <= 100, a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9, and kq is the sum of the differences between the largest and smallest elements in the sorted list a, repeated for the first half of the list, for each iteration of the loop.
#Overall this is what the function does:The function `func` reads an integer `ntest` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It sorts the list `a` and calculates the sum of the differences between the largest and smallest elements in the sorted list, repeated for the first half of the list. This sum, `kq`, is printed for each test case. The function does not return any value. After the function concludes, `ntest` is the number of test cases processed, `n` is the last read number of elements, `a` is the last sorted list of integers, and `kq` is the last calculated sum of differences for the current test case.

