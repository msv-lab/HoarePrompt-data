#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: After all iterations, `i` is equal to `len(a) // 2`, `a` is a sorted list of integers, and `kq` is the total sum of the differences between each pair of elements from the end and the start of the list `a`, covering all pairs up to the middle of the list.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer t (number of test cases) followed by a list of n integers. For each test case, it sorts the list of integers and calculates the sum of differences between corresponding elements from the start and the end of the sorted list, up to the middle of the list. Finally, it prints the calculated sum for each test case.

