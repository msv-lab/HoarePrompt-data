#State of the program right berfore the function call: **
def func():
    n, n1, n2 = (int(i) for i in raw_input().split())
    a = [int(i) for i in raw_input().split()]
    a.sort()
    if (n1 > n2) :
        n1, n2 = n2, n1
    #State of the program after the if block has been executed: *`n`, `n1`, and `n2` are input integers stored in list `a` in ascending order. If `n1` is greater than `n2`, the function maintains the ascending order of the list `a`.
    s1 = 0
    for i in range(n1):
        s1 += a[n - i - 1]
        
    #State of the program after the  for loop has been executed: `n`, `n1`, and `n2` are input integers stored in list `a` in ascending order, `s1` is the sum of the last `n1` elements in list `a`
    s2 = 0
    for i in range(n2):
        s2 += a[n - n1 - i - 1]
        
    #State of the program after the  for loop has been executed: Output State: `n`, `n1`, and `n2` are input integers stored in list `a` in ascending order, `s1` is the sum of the last `n1` elements in list `a`, `s2` is the sum of elements calculated by the loop, where `s2` is the sum of the last `n2` elements in list `a`.
    print(1.0 * s1 / n1 + 1.0 * s2 / n2)
#Overall this is what the function does:The function `func` reads three integers as input, sorts the second integer to be smaller than the third if initially greater, calculates the sum of the last `n1` elements in the sorted list `a`, then calculates the sum of the last `n2` elements in `a`, and finally prints the average of these two sums divided by their respective counts `n1` and `n2`. The function does not accept any parameters and does not return any value.

