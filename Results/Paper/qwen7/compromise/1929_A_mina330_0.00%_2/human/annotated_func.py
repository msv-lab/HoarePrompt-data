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
        
    #State: The loop has completed all its iterations. `a` is a sorted list of integers, `i` is equal to `len(a)`, and `kq` is the sum of `a[len(a) - i - 1] - a[i]` for all iterations from `i=0` to `i=len(a)//2-1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer n and a list of n integers a. It sorts the list a in ascending order and then calculates the sum of differences between elements symmetrically from the ends of the list towards the center. Specifically, for each element pair (a[i], a[len(a)-i-1]) where i ranges from 0 to len(a)//2-1, it adds the difference a[len(a)-i-1] - a[i] to the total sum kq. After processing all test cases, it prints the final value of kq for each case.

