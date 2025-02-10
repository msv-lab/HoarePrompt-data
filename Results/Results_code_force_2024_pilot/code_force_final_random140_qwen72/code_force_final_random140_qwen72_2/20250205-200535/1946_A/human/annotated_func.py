#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 10^5, representing the length of the array a, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is 0, `n` and `a` are undefined (as they are re-initialized in each iteration), and the results of the operations (values of `res`) for each test case have been printed.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` followed by a list of `n` integers `a`. For each test case, the function sorts the list `a`, finds the median value, and counts how many times this median value appears in the sorted list from the median position onwards. The function then prints the count for each test case. After processing all test cases, the function completes, and the state of the program is such that `t` is 0, and the variables `n` and `a` are undefined for the next test case.

