#State of the program right berfore the function call: n, n1, and n2 are integers such that 1 <= n, n1, n2 <= 100000 and n1 + n2 <= n. ai is an integer such that 1 <= ai <= 100000 for each i.**
def func():
    n, n1, n2 = (int(i) for i in raw_input().split())
    a = [int(i) for i in raw_input().split()]
    a.sort()
    if (n1 > n2) :
        n1, n2 = n2, n1
    #State of the program after the if block has been executed: *`n`, `n1`, `n2` are integers within the specified range; `a` is a list of integers sorted in ascending order. If `n1` is greater than `n2`, the program does not modify any variables and retains their initial values.
    s1 = 0
    for i in range(n1):
        s1 += a[n - i - 1]
        
    #State of the program after the  for loop has been executed: `n`, `n1`, `n2` are integers within the specified range; `a` is a list of integers sorted in ascending order; `s1` is the sum of integers in the list `a` starting from the index `n - n1 - 1` after all iterations of the loop have finished. If `n1` is greater than `n`, `s1` remains 0.
    s2 = 0
    for i in range(n2):
        s2 += a[n - n1 - i - 1]
        
    #State of the program after the  for loop has been executed: `n`, `n1`, `n2` are integers within the specified range; `a` is a list of integers sorted in ascending order; `s1` is the sum of integers in the list `a` starting from the index `n - n1 - 1` after all iterations of the loop have finished. If `n1` is greater than `n`, `s1` remains 0; `s2` is the sum of `n2` integers from the list `a` starting from the index `n - n1 - 1`.
    print(1.0 * s1 / n1 + 1.0 * s2 / n2)
#Overall this is what the function does:The function accepts inputs n, n1, n2, and a list of integers. It sorts the list in ascending order and calculates the sum of the n1 smallest elements as s1 and the sum of the n2 largest elements as s2. Then, it prints the average of s1/n1 and s2/n2. If n1 is greater than n, s1 will be 0. The function calculates the average of the sums of the specified elements.

