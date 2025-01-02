#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, m is an integer such that 1 ≤ m ≤ 10,000, and a list of integers a_i of length n where each a_i satisfies 1 ≤ a_i ≤ 100.
def func():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    a = [0] * n
    for i in range(n):
        a[i] = int(sys.stdin.readline())
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `m` is an integer (1 ≤ m ≤ 10,000), `a_i` is a list of integers of length `n` where each `a_i` satisfies 1 ≤ a_i ≤ 100, `a` is a list of length `n` where each element `a[i]` (0 ≤ i < n) is set to an integer read from the standard input (1 ≤ a[i] ≤ 100).
    asort = sorted(a, reverse=True)
    numspacesremaining = asort[0] * (n - 1) - sum(asort[1:])
    if (m <= numspacesremaining) :
        mink = max(asort)
    else :
        mink = max(asort) + max(math.ceil((m - numspacesremaining) / float(n)), 0)
    #State of the program after the if-else block has been executed: *`n` is an integer (1 ≤ n ≤ 100), `m` is an integer (1 ≤ m ≤ 10,000), `a_i` is a list of integers of length `n` where each `a_i` satisfies 1 ≤ a_i ≤ 100, `a` is a list of length `n` where each element `a[i]` (0 ≤ i < n) is set to an integer read from the standard input (1 ≤ a[i] ≤ 100), `asort` is a list of length `n` containing the elements of `a` sorted in descending order, `numspacesremaining` is `asort[0] * (n - 1) - sum(asort[1:])`. If `m` is less than or equal to `numspacesremaining`, `mink` is `asort[0]`. Otherwise, `mink` is `max(asort[0], math.ceil((m - numspacesremaining) / float(n)))`.
    maxk = max(a) + m
    print(str(int(mink)) + ' ' + str(maxk))
#Overall this is what the function does:The function reads inputs `n`, `m`, and a list `a` of `n` integers from the standard input, where `1 ≤ n ≤ 100`, `1 ≤ m ≤ 10,000`, and each `a_i` satisfies `1 ≤ a_i ≤ 100`. It then calculates two values, `mink` and `maxk`, and prints them separated by a space. `mink` is determined based on the available space (`numspacesremaining`) calculated as the difference between the product of the largest element in `a` and `(n-1)` and the sum of the remaining elements in `a` when sorted in descending order. If `m` is less than or equal to `numspacesremaining`, `mink` is set to the largest element in `a`; otherwise, `mink` is the largest element in `a` plus the ceiling of the quotient of the difference between `m` and `numspacesremaining` divided by `n`. `maxk` is simply the largest element in `a` plus `m`. The function does not return any value; instead, it directly prints the results. Edge cases include scenarios where `n` is 1 or `m` is 0, which should still be handled correctly by the function.

