#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the second line of the input contains n integers a_i such that 1 ≤ a_1 < a_2 < ... < a_n ≤ 10^3.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `a` is a list containing `n` integers such that \(1 \leq a_1 < a_2 < \ldots < a_n \leq 10^3\), `max_erase` is the maximum of the differences `a[i] - a[i - 1] - 1` for all `i` from 1 to `n-1`.
    print(max_erase)
#Overall this is what the function does:The function accepts an integer \(n\) such that \(1 \leq n \leq 100\) and a list of \(n\) integers \(a_i\) such that \(1 \leq a_1 < a_2 < \ldots < a_n \leq 10^3\). It calculates and prints the maximum value of \(a[i] - a[i - 1] - 1\) for all \(i\) from 1 to \(n-1\). The function does not handle cases where \(n\) is less than 2 or when the input list does not strictly increase. If \(n = 1\), the function will print 0 because there are no pairs to compare.

