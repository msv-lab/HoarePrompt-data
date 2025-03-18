#State of the program right berfore the function call: t is a positive integer, and for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5 and the array a contains n integers where each integer is in the range 1 ≤ a_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a.count(a[p])
        
        print(res)
        
    #State: Output State: t is an input integer, n is a positive integer such that 1 ≤ n ≤ 10^5, and for each iteration of the loop, the variable res contains the count of the median element in the sorted list a.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `n` and an array `a` of `n` integers. For each test case, it sorts the array and calculates the count of the median element in the sorted array. It then prints this count for each test case.

