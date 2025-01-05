#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100000, and a is a list of n integers where each integer ai satisfies 1 ≤ ai ≤ 100000.
def func():
    ti = lambda : stdin.readline().strip()
    ma = lambda fxn, ti: map(fxn, ti.split())
    ol = lambda arr: stdout.write(' '.join(str(i) for i in arr) + '\n')
    os = lambda i: stdout.write(str(i) + '\n')
    olws = lambda arr: stdout.write(''.join(str(i) for i in arr) + '\n')
    n = int(ti())
    a = ma(int, ti())
    freq = [0] * (10 ** 5 + 1)
    for i in range(n):
        freq[a[i]] += 1
        
    #State of the program after the  for loop has been executed: `freq` is a list where `freq[k]` is the count of occurrences of integer `k` in the list `a`, `n` is the integer input, and `a` is a list of integers from the input.
    dp = [0, freq[1]]
    for i in range(2, n + 1):
        dp.append(max(dp[i - 1], dp[i - 2] + freq[i] * i))
        
    #State of the program after the  for loop has been executed: `freq` is a list where `freq[k]` is the count of occurrences of integer `k` in the list `a`, `n` is a positive integer, `dp` is updated to contain the maximum points possible from the values in `freq` for integers from 0 to `n`.
    os(dp[n])
#Overall this is what the function does:The function accepts a positive integer `n` and a list of `n` integers, counts the occurrences of each integer in the list, and calculates the maximum points possible by selecting integers such that no two adjacent integers are selected. It outputs the maximum points computed from the list.

