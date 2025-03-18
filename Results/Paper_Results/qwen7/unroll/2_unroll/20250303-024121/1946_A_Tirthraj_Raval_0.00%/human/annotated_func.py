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
        
    #State: Output State: t is the number of test cases, and for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and the array a contains n integers where each integer is in the range 1 ≤ a_i ≤ 10^9. After sorting the array a, p is set to (n + 1) // 2 - 1, and res is the count of the element at index p in the sorted array a. The loop prints res for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer `n` and an array `a` of `n` integers. It then sorts the array and calculates the count of the middle element (if `n` is odd) or the lower of the two middle elements (if `n` is even). The function outputs this count for each test case.

