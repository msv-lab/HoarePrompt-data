#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, n is an integer such that 2 ≤ n ≤ 100, and a is a list of n integers where 1 ≤ a_i ≤ 10^9.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 500, `n` is the last input integer read, `a` is the last list of integers read and sorted, `ntest` is the same input integer, and `kq` is the sum of the differences between the largest and smallest elements of the last list `a` for the first half of the list.
#Overall this is what the function does:The function reads an integer `ntest` indicating the number of test cases, and for each test case, it reads an integer `n` and a list `a` of `n` integers. It sorts the list `a` and calculates the sum of the differences between the largest and smallest elements of the first half of the sorted list. This sum is printed for each test case. The function does not return any value. After the function concludes, `ntest` remains the same, `n` is the last input integer read, `a` is the last list of integers read and sorted, and the sum of the differences for the last test case is printed.

