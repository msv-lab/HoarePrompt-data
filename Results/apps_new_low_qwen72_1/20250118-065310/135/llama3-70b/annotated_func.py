#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    if (n == 1) :
        print(-1)
    else :
        for m in range(n, int(1e+18) + 1):
            k = (m ** 2 - n ** 2) ** 0.5
            
            if k == int(k):
                print(m, int(k) + n)
                break
            
        #State of the program after the  for loop has been executed: If an integer `k` is found, the loop prints `(m, int(k) + n)` and breaks. If no such `m` is found within the range, the loop prints `-1`.
    #State of the program after the if-else block has been executed: *`n` is an input integer such that 1 ≤ n ≤ 10^9. If `n` is 1, the function does nothing specific (assuming no action is taken in the if part). Otherwise, if an integer `k` is found, the loop prints `(m, int(k) + n)` and breaks. If no such `m` is found within the range, the loop prints `-1`.
#Overall this is what the function does:The function `func` accepts an integer `n` where 1 ≤ n ≤ 10^9 and performs the following actions:

1. If `n` is 1, it prints `-1`.
2. If `n` is greater than 1, it searches for the smallest integer `m` starting from `n` up to 10^18 such that the expression `(m^2 - n^2)^0.5` results in an integer `k`. When such an `m` and `k` are found, it prints the tuple `(m, int(k) + n)` and exits the loop.
3. If no such `m` is found within the specified range, it prints `-1`.

The function does not return any value; it only prints the result to the console. The state of the program after the function concludes is that either a tuple `(m, int(k) + n)` has been printed, or `-1` has been printed, depending on the input `n` and the search for `m` and `k`.

