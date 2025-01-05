#State of the program right berfore the function call: n is a positive integer. The sequence a consists of n integers such that each integer is between 1 and 105 (inclusive).**
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
        
    #State of the program after the  for loop has been executed: freq contains the frequency of each unique element in the list a after all iterations of the loop have finished
    dp = [0, freq[1]]
    for i in range(2, n + 1):
        dp.append(max(dp[i - 1], dp[i - 2] + freq[i] * i))
        
    #State of the program after the  for loop has been executed: `freq` contains the frequency of each unique element in the list `a`, `dp` is a list containing the maximum value between the previous two elements of `dp` and the sum of the product of the frequency of the element at index `i` and `i` with the value at index `i-2` in `dp` for each index `i` from 0 to `n`
    os(dp[n])
#Overall this is what the function does:The function reads a positive integer `n` representing the number of elements in a sequence. It then reads `n` integers into a list `a` where each integer is between 1 and 105 (inclusive). The function calculates the frequency of each unique element in the list `a` and stores it in a list `freq`. It then computes a list `dp` where each element is the maximum value between the previous two elements of `dp` and the sum of the product of the frequency of the element at that index and the index itself. Finally, the function outputs the value at index `n` in the list `dp`.

