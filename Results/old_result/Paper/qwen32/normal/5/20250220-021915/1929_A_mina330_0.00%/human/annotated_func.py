#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the array a contains n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
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
        
    #State: `ntest` is an integer such that 1 ≤ `ntest` ≤ 500, `itest` is `ntest - 1`, `n` is an input integer, `a` is a sorted list of integers read from the input, `kq` is the sum of `a[len(a) - i - 1] - a[i]` for all `i` from `0` to `len(a) // 2 - 1`, `i` is `len(a) // 2 - 1`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. It sorts the list and calculates the sum of differences between the largest and smallest elements, the second largest and second smallest elements, and so on, up to the middle of the list. The result for each test case is printed.

