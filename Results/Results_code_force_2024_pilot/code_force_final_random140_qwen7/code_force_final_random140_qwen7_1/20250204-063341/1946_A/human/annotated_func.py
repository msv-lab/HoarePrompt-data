#State of the program right berfore the function call: t is a positive integer, and for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and the array a contains n integers where 1 ≤ a_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        
        a = list(map(int, input().strip().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a[p:].count(a[p])
        
        print(res)
        
    #State: t is 0 or greater, `n` is an integer input from the user, `a` is a list of integers sorted in ascending order, `p` is (n + 1) // 2 - 1, and `res` is the count of `a[p]` in the subarray `a[p:]` after all iterations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t`, followed by an integer `n` and an array `a` of `n` integers. It sorts the array `a` in ascending order, calculates the middle index `p` based on `n`, and counts the occurrences of the element at index `p` in the subarray starting from `p`. Finally, it prints the count for each test case.

