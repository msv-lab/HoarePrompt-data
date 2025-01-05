#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10^5) followed by n integers a1, a2, ..., an (1 ≤ ai ≤ 10^5).
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
        
    #State of the program after the  for loop has been executed: `freq` is a list where `freq[i]` is the count of occurrences of integer `i` in `a`, `n` is the length of the list `a`, and `a` is a list of integers.
    dp = [0, freq[1]]
    for i in range(2, n + 1):
        dp.append(max(dp[i - 1], dp[i - 2] + freq[i] * i))
        
    #State of the program after the  for loop has been executed: `dp` is a list where `dp[0]` is 0, `dp[1]` is the count of occurrences of integer 1 in `a`, and `dp[i]` is the maximum value calculated based on the occurrences of integers from 1 to `n`, `freq` is a list where `freq[i]` is the count of occurrences of integer `i` in `a`, and `n` is the length of the list `a`.
    os(dp[n])
#Overall this is what the function does:The function accepts an integer `n` followed by `n` integers, counts the occurrences of each integer from 1 to 100,000, and computes the maximum sum of non-adjacent integers using a dynamic programming approach, returning this maximum sum. It correctly handles cases where the input integers and their counts are within the specified range.

