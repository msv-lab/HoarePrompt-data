#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 10^5) representing the length of the array, and an array a of n integers (1 ≤ a_i ≤ 10^9). The total number of test cases t is given (1 ≤ t ≤ 10^4), and the sum of the values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has completed all iterations. The function `func` has processed all test cases, and for each test case, it has printed the count of the middle element in the sorted array `a`. The variables `t`, `n`, `a`, `p`, and `res` have been used within the loop, but their final values are not retained after the loop finishes.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and an array `a` of `n` integers, sorts the array, and prints the count of the middle element in the sorted array. The function does not return any values; it only prints the results. After processing all test cases, the function concludes without retaining the final values of any variables used within the loop.

