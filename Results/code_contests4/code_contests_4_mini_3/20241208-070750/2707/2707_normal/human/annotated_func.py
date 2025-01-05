#State of the program right berfore the function call: n, n1, and n2 are integers such that 1 ≤ n, n1, n2 ≤ 100,000 and n1 + n2 ≤ n; a is a list of n integers where each integer ai satisfies 1 ≤ ai ≤ 100,000.
def func():
    n, n1, n2 = (int(i) for i in raw_input().split())
    a = [int(i) for i in raw_input().split()]
    a.sort()
    if (n1 > n2) :
        n1, n2 = n2, n1
    #State of the program after the if block has been executed: *`n`, `n1`, `n2` are integers, and `a` is a sorted list of `n` integers. If `n1` is greater than `n2`, then `n1` is updated to the previous value of `n2`, `n2` is updated to the previous value of `n1`, and `a` remains a sorted list of `n` integers.
    s1 = 0
    for i in range(n1):
        s1 += a[n - i - 1]
        
    #State of the program after the  for loop has been executed: `n` is an integer, `n1` is an integer, `n2` is an integer, `a` is a sorted list of `n` integers, `s1` is the sum of the last `min(n1, n)` elements of `a`.
    s2 = 0
    for i in range(n2):
        s2 += a[n - n1 - i - 1]
        
    #State of the program after the  for loop has been executed: `n` is an integer, `n1` is an integer, `n2` is greater than or equal to 0, `a` is a sorted list of `n` integers, `s1` is the sum of the last `min(n1, n)` elements of `a`, `s2` is the sum of the last `min(n2, n1)` elements of `a`, `i` is `n2 - 1`.
    print(1.0 * s1 / n1 + 1.0 * s2 / n2)
#Overall this is what the function does:The function accepts three integers, `n`, `n1`, and `n2`, and a list `a` of `n` integers. It calculates the average of the largest `n1` elements and the next largest `n2` elements from the sorted list `a`, returning the sum of these two averages. If `n1` is greater than `n2`, their values are swapped. The function may not handle cases where `n1` or `n2` is zero, which could lead to division by zero errors. Additionally, it assumes that `n1 + n2` is less than or equal to `n`, which should be validated.

