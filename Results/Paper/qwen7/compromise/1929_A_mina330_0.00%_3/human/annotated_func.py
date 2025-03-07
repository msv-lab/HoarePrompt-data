#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9.
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
        
    #State: `ntest` remains the same as the initial input integer, `itest` remains the same as `ntest`, `t` remains a positive integer within the range of 1 to 500, `n` remains the same as the initial input integer, `a` remains a list of integers sorted in non-decreasing order, `kq` is the sum of the differences between the last half and the first half of the list `a`, and `i` is equal to `len(a) // 2` after the loop completes all its iterations.
#Overall this is what the function does:The function processes multiple test cases, each containing a positive integer t (indicating the number of subsequent test instances), followed by t sets of data. Each set consists of an integer n and a list of n integers. For each set, the function sorts the list of integers in non-decreasing order, calculates the sum of the differences between the last half and the first half of the sorted list, and prints this sum for each set.

