#State of the program right berfore the function call: n, n1, and n2 are integers such that 1 <= n, n1, n2 <= 100,000 and n1 + n2 <= n. The list of integers a1, a2, ..., an contains wealth values such that 1 <= ai <= 100,000 for each i.**
def func():
    n, n1, n2 = (int(i) for i in raw_input().split())
    a = [int(i) for i in raw_input().split()]
    a.sort()
    if (n1 > n2) :
        n1, n2 = n2, n1
    #State of the program after the if block has been executed: *n, n1, n2 are integers such that 1 <= n, n1, n2 <= 100,000 and n1 + n2 <= n, the list `a` contains the wealth values sorted in ascending order. After the execution of the if else block, if n1 > n2, n1 and n2 have been swapped.
    s1 = 0
    for i in range(n1):
        s1 += a[n - i - 1]
        
    #State of the program after the  for loop has been executed: `n`, `n1`, `n2` are integers such that 1 <= `n`, `n1`, `n2` <= 100,000 and `n1` + `n2` <= `n`, `a` contains the wealth values sorted in ascending order, `s1` is the sum of wealth values from position (`n - n1`) to the last position in the list `a`.
    s2 = 0
    for i in range(n2):
        s2 += a[n - n1 - i - 1]
        
    #State of the program after the  for loop has been executed: `n`, `n1`, `n2` are integers such that 1 <= `n`, `n1`, `n2` <= 100,000 and `n1` + `n2` <= `n`, `a` contains the wealth values sorted in ascending order, `s1` is the sum of wealth values from position (`n - n1`) to the last position in the list `a`, `s2` is the sum of wealth values from position (`n - n1`) to the last position in the list `a` plus the sum of the wealth values at positions (`n - n1 - 1`) to (`n - n1 - n2`)
    print(1.0 * s1 / n1 + 1.0 * s2 / n2)
#Overall this is what the function does:The function `func` reads input values `n, n1, n2` and a list of integers `a` and calculates the average of two sums of wealth values based on the indices `n - n1` and `n - n1 - n2`. The function does not return any specific value. If `n1` is greater than `n2`, the function swaps their values before performing the calculations.

