#State of the program right berfore the function call: n, n1, and n2 are integers such that 1 ≤ n, n1, n2 ≤ 100,000 and n1 + n2 ≤ n; a is a list of n integers where each integer ai satisfies 1 ≤ ai ≤ 100,000.
def func():
    n, n1, n2 = (int(i) for i in raw_input().split())
    a = [int(i) for i in raw_input().split()]
    a.sort()
    if (n1 > n2) :
        n1, n2 = n2, n1
    #State of the program after the if block has been executed: *`n`, `n1`, and `n2` are integers. If `n1` is greater than `n2`, then `n1` takes the previous value of `n2`, `n2` takes the previous value of `n1`, and `a` remains a sorted list of integers.
    s1 = 0
    for i in range(n1):
        s1 += a[n - i - 1]
        
    #State of the program after the  for loop has been executed: `s1` is equal to the sum of the last `n1` elements of the sorted list `a`, `n1` is the number of elements summed, `n` is greater than or equal to `n1`, `a` is a sorted list of integers.
    s2 = 0
    for i in range(n2):
        s2 += a[n - n1 - i - 1]
        
    #State of the program after the  for loop has been executed: `s1` is equal to the sum of the last `n1` elements of the sorted list `a`; `n1` is the number of elements summed; `n` is greater than or equal to `n1`; `s2` is equal to the sum of the last `n2` elements of the sorted list `a` starting from index `n - n1 - 1`; `n2` is the number of iterations completed; `i` is equal to `n2 - 1` after the loop completes.
    print(1.0 * s1 / n1 + 1.0 * s2 / n2)
#Overall this is what the function does:The function accepts three integers `n`, `n1`, and `n2`, and a list `a` of `n` integers. It calculates the average of the largest `n1` integers and the next largest `n2` integers from the sorted list `a`, printing the sum of these averages. It assumes valid input according to the constraints provided, without handling invalid input cases.

