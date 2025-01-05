#State of the program right berfore the function call: **
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
        
    #State of the program after the  for loop has been executed: Output State: `ti` is a lambda function that reads input and strips whitespaces, `olws` is a lambda function that writes the elements of an array to the standard output with a newline character, `n` is an input integer greater than 0, `a` is the integer value of the input after applying the `int` function, `freq` is a list where each element represents the frequency of a corresponding integer value in the input array `a`, `i` is equal to `n-1`
    dp = [0, freq[1]]
    for i in range(2, n + 1):
        dp.append(max(dp[i - 1], dp[i - 2] + freq[i] * i))
        
    #State of the program after the  for loop has been executed: `ti` is a lambda function, `olws` is a lambda function, `n` is an input integer greater than or equal to 3, `a` is an integer value, `freq` is a list representing the frequency of integer values in `a`, `i` is equal to `n-1`, `dp` is a list containing the maximum values between the last two elements of `dp` for each index from 0 to `n`.
    os(dp[n])
#Overall this is what the function does:The function reads an integer `n` from input, followed by an array of integers `a`. It then calculates the frequency of each integer in `a` and uses dynamic programming to find the maximum sum based on the frequencies and values of integers. Finally, it outputs the maximum sum calculated. The function does not accept any parameters and does not return any value.

