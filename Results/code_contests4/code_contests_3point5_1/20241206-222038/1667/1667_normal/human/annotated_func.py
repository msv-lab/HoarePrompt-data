#State of the program right berfore the function call: n is a positive integer. The sequence a consists of n integers where each integer is between 1 and 105 (inclusive).**
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
        
    #State of the program after the  for loop has been executed: `n` is assigned the value of the integer returned by `ti()` function, `a` consists of `n` integers between 1 and 105 (inclusive), `freq` is a list of 100001 elements with the value at index `a[i]` increased by the frequency of `a[i]` in the list `a`
    dp = [0, freq[1]]
    for i in range(2, n + 1):
        dp.append(max(dp[i - 1], dp[i - 2] + freq[i] * i))
        
    #State of the program after the  for loop has been executed: `n` is assigned the value of the integer returned by `ti()` function, `a` consists of `n` integers between 1 and 105 (inclusive), `freq` is updated based on the elements in `a`, `dp` is a list containing the maximum values calculated based on the elements in `a` and their frequencies
    os(dp[n])
#Overall this is what the function does:The function `func` reads an integer `n` representing the length of a sequence and a sequence of `n` integers. It then calculates the maximum value based on the elements in the sequence and their frequencies. The function does not accept any parameters explicitly, but it operates on the input sequence to determine the maximum value.

