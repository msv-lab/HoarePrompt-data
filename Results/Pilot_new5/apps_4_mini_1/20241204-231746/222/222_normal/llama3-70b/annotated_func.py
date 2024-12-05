#State of the program right berfore the function call: n is a positive integer (1 <= n <= 1000) representing the number of skewers, and k is a non-negative integer (0 <= k <= 1000) representing the number of skewers turned on each side during one action.
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 <= n <= 1000), `k` is a non-negative integer (0 <= k <= 1000), `l` is the final value of `(n + k - 1) // (k * 2 + 1)`, `i` is `l - 1`, and `res` includes the values from `1` to `l * (k * 2 + 1) + 1` with a common difference of `(k * 2 + 1)`.
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function accepts two integers, `n` (a positive integer representing the number of skewers) and `k` (a non-negative integer representing the number of skewers turned on each side during one action). It calculates the minimum number of actions required to handle `n` skewers based on `k` and prints this number. Additionally, it prints a list of positions that represent the first skewer turned on in each action, following an arithmetic sequence with a common difference of `(k * 2 + 1)`. The function does not return any value but prints the results directly.

