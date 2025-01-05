#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100,000; n1 and n2 are integers such that 1 ≤ n1, n2 ≤ 100,000 and n1 + n2 ≤ n; a is a list of integers representing the wealth of candidates, where each wealth value ai satisfies 1 ≤ ai ≤ 100,000.
def func():
    n, n1, n2 = (int(i) for i in raw_input().split())
    a = [int(i) for i in raw_input().split()]
    a.sort()
    if (n1 > n2) :
        n1, n2 = n2, n1
    #State of the program after the if block has been executed: *`a` is a list of integers sorted in ascending order. If `n1` is greater than `n2`, then after the swap, `n1` is less than `n2`. If `n1` is not greater than `n2`, the list `a` remains unchanged.
    s1 = 0
    for i in range(n1):
        s1 += a[n - i - 1]
        
    #State of the program after the  for loop has been executed: `s1` is the sum of the last `n1` elements of the list `a`, where `n1` is less than or equal to the length of `a`, and `i` is `n1 - 1`.
    s2 = 0
    for i in range(n2):
        s2 += a[n - n1 - i - 1]
        
    #State of the program after the  for loop has been executed: `s1` is the sum of the last `n1` elements of the list `a`, `i` is `n2 - 1`, `s2` is increased by the sum of the last `n2` elements starting from `a[n - n1 - n2]` to `a[n - n1 - 1]`, where `n2` is less than or equal to the length of the sublist of `a` starting from `n - n1`.
    print(1.0 * s1 / n1 + 1.0 * s2 / n2)
#Overall this is what the function does:The function accepts three integers `n`, `n1`, `n2` and a list of integers `a`, representing the wealth of candidates. It calculates the average wealth of the top `n1` wealthiest candidates and the top `n2` wealthiest candidates (after sorting the list in ascending order), and then outputs the sum of these averages. The function does not return any value but prints the result directly.

