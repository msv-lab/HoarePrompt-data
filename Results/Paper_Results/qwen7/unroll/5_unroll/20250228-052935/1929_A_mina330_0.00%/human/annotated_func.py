#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: The sum of the differences between the largest and smallest elements, the second largest and second smallest elements, and so on, for each test case provided by the input. This process is repeated for each of the ntest test cases.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers `a`. It then sorts the list of integers and calculates the sum of the differences between the largest and smallest elements, the second largest and second smallest elements, and so on. Finally, it prints the calculated sum for each test case.

