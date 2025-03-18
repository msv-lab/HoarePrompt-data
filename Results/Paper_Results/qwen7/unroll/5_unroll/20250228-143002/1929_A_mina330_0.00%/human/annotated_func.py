#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: The value of `kq` is the sum of the differences between the largest and smallest elements, the second largest and second smallest elements, and so on, for each pair of elements in the list `a`, for each test case defined by `ntest`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a positive integer t (though t is not used in the function), an integer n, and a list of n integers a_1, a_2, ..., a_n. It sorts the list of integers, then calculates the sum of the differences between the largest and smallest elements, the second largest and second smallest elements, and so on, for each pair of elements in the list. Finally, it prints the calculated sum for each test case.

