#State of the program right berfore the function call: n is an integer in the range 1 to 100,000 (1 ≤ n ≤ 10^5), and the sequence a consists of n integers where each integer ai is in the range 1 to 100,000 (1 ≤ ai ≤ 10^5).
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer in the range 1 to 100,000, `freq` is a list where each index corresponds to a value in `a`, and `freq[i]` represents the count of occurrences of the value `i` in the list `a`.
    dp = [0, freq[1]]
    for i in range(2, n + 1):
        dp.append(max(dp[i - 1], dp[i - 2] + freq[i] * i))
        
    #State of the program after the  for loop has been executed: `dp` is a list where the last element is the maximum value calculated based on the frequencies in `freq`, and `n` is an integer in the range 1 to 100,000.
    os(dp[n])
#Overall this is what the function does:The function accepts an integer `n`, which represents the number of integers in the sequence, and a sequence of `n` integers ranging from 1 to 100,000. It calculates the maximum sum of values by considering the frequency of each integer while ensuring that no two adjacent integers are counted. The function returns this maximum sum as output.

